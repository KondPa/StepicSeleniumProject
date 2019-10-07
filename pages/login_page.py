from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "/login" in url, f"Page should contain 'login' but it is '{url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Have not found Form itself"
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "Login email field is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Login password field is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOT_PASSWORD_LINK), "Login forgotten password" \
                                                                                       "link is not present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Have not found Form itself"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_FIELD), "Registration email field is not " \
                                                                                     "present "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD), "Registration password field " \
                                                                                        "is not present "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_FIELD), "Registration confirm " \
                                                                                                "password field is " \
                                                                                                "not present "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not present"

    def register_new_user(self, email, password):
        emailfield = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        emailfield.send_keys(str(email))
        passwordfield = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        passwordfield.send_keys(str(password))
        repeatofpasswordfield = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_FIELD)
        repeatofpasswordfield.send_keys(str(password))
        registrationbutton = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registrationbutton.click()
