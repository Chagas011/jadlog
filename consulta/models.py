
# Create your models here.
from django.db import models


class Pedidos(models.Model):
    nome_cliente = models.CharField(max_length=255)
    data = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    prazo = models.IntegerField(
        choices=(
            (2, '2 dias'),
            (3, '3 dias'),
            (5, '5 dias'),
            (7, '7 dias'),
            (15, '15 dias')
        )
        )
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='SP',

        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
            )
    )
    cep_origem = models.CharField(max_length=8)
    endereco_origem = models.CharField(max_length=255)
    cep_destino = models.CharField(max_length=8)
    endereco_destino = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome_cliente
