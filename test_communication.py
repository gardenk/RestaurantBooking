from communication import SmsSender, MailSender


class TestableSmsSender(SmsSender):
    def send(self, schedule):
        print("테스트용 smsSender")
        self.__send_method_is_called = True

    def is_send_method_is_called(self):
        return self.__send_method_is_called


class TestableMailSender(MailSender):
    def __init__(self):
        self.__count_send_mail_is_called = 0

    def send_mail(self, schedule):
        print("테스트용 MailSender")
        self.__count_send_mail_is_called += 1

    def get_count_send_mail_is_called(self):
        return self.__count_send_mail_is_called
