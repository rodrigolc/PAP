from django.test import TestCase

from usuarios.models import *  # importa os models para os testes

# Create your tests here.


class TokenTestCase(TestCase):
    def setUp(self):
        convite = TokenConvite()
        convite.token = "TOKEN123123"
        convite.save()

    def testTokenJaExiste(self):
        convite = TokenConvite()
        convite.token = "TOKEN123123"
        self.assertRaisesMessage(Exception, "Token Já Existe", convite.save)

    def testTokenJaUsado(self):
        convite = TokenConvite()
        convite.token = "TOKENUSADO"
        convite.usado = True
        convite.save()

        user = User(login='user1', password='pass1')
        user.save()
        aluno = Aluno()
        aluno.user = user
        aluno.token = convite
        self.assertRaisesMessage(Exception, "Token Já Utilizado", aluno.save())


class UsuarioTestCase(TestCase):
    def setUp(self):
        convite = TokenConvite()
        convite.token = "TOKEN123123"
        convite.save()

    def testCreateUser(self):
        user = User(login='user1', password='pass1')
        user.save()
        aluno = Aluno()
        aluno.user = user
        aluno.token = TokenConvite.objects.get(token="TOKEN123123")
        aluno.save()
        self.assertEquals(True, True)
