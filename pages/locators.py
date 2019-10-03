from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "#login_form a")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    PRODUCT_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, "button.btn-wishlist")
    PRODUCT_WRITE_REVIEW_BUTTON = (By.CSS_SELECTOR, "#write_review")
    PRODUCT_HEADER_CART_INFO = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_BASKET_ALERT = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_HEADER_GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group > a")
    PRODUCT_ALERT_NAME_OF_ADDED_GOOD = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    PRODUCT_ALERT_GO_TO_BASKET = (By.CSS_SELECTOR, ".alertinner a.btn-info:nth-child(1)")
    PRODUCT_ALERT_GO_TO_CHECKOUT = (By.CSS_SELECTOR, ".alertinner a.btn-info:nth-child(2)")
