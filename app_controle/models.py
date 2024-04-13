from django.db import models
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import pre_save
from validate_docbr import CNH
# Create your models here.


class Motorista(models.Model):
    cod_motorista = models.AutoField(verbose_name="Id", primary_key=True, null=False, blank=False)
    nome = models.CharField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    num_cnh = models.CharField(verbose_name="N° da CNH",max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return f"Nome: {self.nome.upper()} || N° da CNH: {self.num_cnh}"
    
    def clean(self):
        cnh = CNH()
        if not cnh.validate(self.num_cnh):
            raise ValidationError("Numero de CNH inválido")

class Veiculo(models.Model):
    cod_veiculo = models.AutoField(verbose_name="Id", primary_key=True, null=False, blank=False)
    placa = models.CharField(max_length=7, null=False, blank=False)
    marca = models.CharField(max_length=20, null=False, blank=False)
    veiculo = models.CharField(max_length=50, null=False, blank=False)
    km_troca_oleo = models.IntegerField(verbose_name="KM próxima troca de Óleo",null=False, blank=False)
    tipo_placa = models.CharField(max_length=20, null=True, blank=True)
    disponivel = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if len(self.placa) == 7:
            if all(map(str.isalpha, self.placa[:3])) and all(map(str.isdigit, self.placa[3:])):
                self.tipo_placa = 'Antigo'
            elif (
                all(map(str.isalpha, self.placa[:3]))
                and str.isdigit(self.placa[3])
                and str.isalpha(self.placa[4])
                and len(self.placa) == 7
                and all(map(str.isdigit, self.placa[5:]))
            ):
                self.tipo_placa = 'Mercosul'
            else:
                raise ValidationError('Placa em formato inválido.')
        else:
            raise ValidationError('Placa em formato inválido.')

    def __str__(self):
        return f"Veículo: {self.marca.upper()} {self.veiculo.upper()} || id: {self.cod_veiculo}"

class Controle(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    data_saida = models.DateField()
    hora_saida = models.TimeField()
    km_saida = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=100)
    data_retorno = models.DateField(null=True, blank=True)
    hora_retorno = models.TimeField(null=True, blank=True)
    km_retorno = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    km_percorrido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def clean(self):

        if self.veiculo.disponivel == False:
            raise ValidationError(f'O Veículo {self.veiculo.marca.upper()} {self.veiculo.veiculo.upper()}, de ID: {self.veiculo.cod_veiculo} já está em uso.')
        super().clean()

        if self.data_saida is not None and self.data_retorno is not None:
            if self.data_retorno < self.data_saida:
                raise ValidationError('ERROR: A Data de Retorno está MENOR que a Data de Saída, insira uma Data MAIOR ou IGUALdo que a Data de Sáida .')
            elif self.data_retorno == self.data_saida and self.hora_retorno is not None and self.hora_saida is not None and self.hora_retorno <= self.hora_saida:
                raise ValidationError('ERROR: A Data de Retorno é Igual a Data de Saída, insira um Horário de Retorno MAIOR que o Horário de Saída.')

        if self.km_saida is not None and self.km_retorno is not None and self.km_retorno <= self.km_saida:
            raise ValidationError('ERROR: A Kilometragem de Retorno deve ser maior que a Kilimetragem de Saida.')
        
        if self.veiculo.km_troca_oleo < self.km_saida:
            raise ValidationError(f"É necessário trocar o óleo do veículo. Proxima troca de óleo é {self.veiculo.km_troca_oleo} Km")
        super().clean()
    
    def calcular_quantidade_dias(self):
        if self.data_retorno is None:
            return None
        data_hora_saida = datetime.combine(self.data_saida, self.hora_saida)
        data_hora_retorno = datetime.combine(self.data_retorno, self.hora_retorno)
        diferenca = data_hora_retorno - data_hora_saida
        return diferenca.days

    def save(self, *args, **kwargs):
        if self.km_saida is not None and self.km_retorno is not None:
            self.km_percorrido = self.km_retorno - self.km_saida
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Controle de {self.veiculo} - {self.data_saida}"
