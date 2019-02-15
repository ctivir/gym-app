# Gender choices

MALE = '1'
FEMALE = '2'
BLANK = ' '

MONTHLY = '1'
WEEKLY = '2'

ACTIVE = '1'
INACTIVE = '2'

CASH = '1'
DEPOSIT = '2'
TRANSFERENCE = '3'

ALL = '1'
MUSCULATION = '2'
GROUP = '3'
SPORT = '4'

GENDER_CHOICES = (
    (MALE, 'Masculino'),
    (FEMALE, 'Feminino'),
    (BLANK, 'Nao especificado')
)

PLAN_CHOICES = (
    (ALL, 'Completo'),
    (MUSCULATION, 'Mosculacao'),
    (GROUP, 'Aulas em grupo'),
    (SPORT, 'Modalidade taykwond'),
)

PAY_CHOICES = (
    (MONTHLY, 'Mensal'),
    (WEEKLY, 'Semanal'),
)

STATUS_CHOICES = (
    (ACTIVE, 'activo'),
    (INACTIVE, 'desactivo')
)
