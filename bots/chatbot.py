from __future__ import unicode_literals
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
import requests
from kivy.uix.label import Label

class ChatScreen(GridLayout):

    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        self.URL = None
        self.selected_chat = None
        self.insult_bot = "297812849:AAFGeKrSX3lyWv3m5XGiu3pr9G6wuLae1E8"
        self.weather_bot = "348367169:AAG4xGta0G35xRPn8nDQYngld12x-rxrCE4"
        self.marilynux = "228030866:AAGFH13_njpLJA2qNhOQDAfaSGxo0y2Ggco"
        self.planbot = "265390616:AAGquQAVoMm0WO7HsmEKPscLwbYNvd3fsdE"
        self.complimentbot = "261401432:AAGLQFIehbRt6zH2TNYTJyvr2PUbnfYRcew"

        self.bots = {"insultbot":self.insult_bot,
                     "planbot":self.planbot,
                     "ilmbot":self.weather_bot,
                     "marilynux":self.marilynux,
                     "complimentbot":self.complimentbot}

        self.chats = {"jaan": "164813180",
                      "clicbait": "-1001071499716",
                      "it7nil2bu": "-1001062124319"}
        self.cols = 1

        self.add_widget(Label(text="Bots"))

        for bot in self.bots:
            btn = ToggleButton(text = bot, group = 'bots')
            btn.bind(on_press=self.botbuttoncallback)
            self.add_widget(btn)

        self.add_widget(Label(text="Chats"))

        for chat in self.chats:
            btn = ToggleButton(text = chat, group = 'chats')
            btn.bind(on_press=self.chatbuttoncallback)
            self.add_widget(btn)

        self.chatbox = TextInput(multiline=True)
        self.add_widget(self.chatbox)

        btn = Button(text = "Send")
        btn.bind(on_press=self.callback)
        self.add_widget(btn)

    def callback(self, instance):
        if self.URL and self.selected_chat and self.chatbox.text:
            self.send_message(self.chatbox.text, self.selected_chat)

    def botbuttoncallback(self, instance):
        self.selection = instance.text
        self.URL = "https://api.telegram.org/bot{}/".format(self.bots[self.selection])
        print self.selection

    def chatbuttoncallback(self, instance):
        self.selected_chat = self.chats[instance.text]
        self.selected_chat_string = instance.text
        print instance.text

    def get_url(self, url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def send_message(self, text, chat_id):
        url = self.URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
        self.get_url(url)
        text = self.selection + "@" + self.selected_chat_string + " " + text
        url = self.URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, self.chats["jaan"])
        self.get_url(url)

class MyApp(App):

    def build(self):
        return ChatScreen()


if __name__ == '__main__':
    MyApp().run()
    #URL = "https://api.telegram.org/bot{}/".format("297812849:AAFGeKrSX3lyWv3m5XGiu3pr9G6wuLae1E8")
    #url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format("botnet", "-158709130")
    
    #requests.get(url)