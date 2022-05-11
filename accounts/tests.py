from django.test import TestCase, Client
from django.contrib.auth.models import User

class LoginRedirectTest(TestCase):
  def setUp(self):
    # テスト用ユーザ作成
    self.credentials = {
      'username': 'testuser',
      'password': 'sampleuser'
    }
    User.objects.create_user(**self.credentials)

    # テストクライアントのインスタンスを設定
    self.client = Client()

  def test_redirect(self):
    '''
    ログインしていない状態の時、リダイレクトされたか確認するテスト
    '''
    response = self.client.get('/', follow=True)
    redirect_url = list(response.redirect_chain[0])[0]
    self.assertEqual(redirect_url, '/accounts/login/?next=/')
  
  def test_not_redirect(self):
    '''
    ログイン状態の時、リダイレクトされないか確認するテスト
    '''
    # テストユーザでログイン
    self.client.login(
      username=self.credentials['username'],
      password=self.credentials['password']
    )
    response = self.client.get('/')
    # リダイレクトされずに画面が開かれること
    self.assertEqual(response.status_code, 200)

      



