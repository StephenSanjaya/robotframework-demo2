#login page locators
txt_username="//android.widget.EditText[@text='Username']"
txt_password="//android.widget.EditText[@text='Password']"
btn_login="//android.view.ViewGroup[@content-desc='test-LOGIN']"
txt_error_message="//android.view.ViewGroup[@content-desc='test-Error message']/android.widget.TextView[@index='0']"
element_error_message="//android.view.ViewGroup[@content-desc='test-Error message']"
element_image_saucedemo="//android.view.ViewGroup/android.widget.ImageView[@index='0']"


#home page locators
txt_title="//android.view.ViewGroup[@content-desc='test-Cart drop zone']/android.view.ViewGroup/android.widget.TextView[@index='0']"
iv_filter="//android.view.ViewGroup[@content-desc='test-Modal Selector Button']/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView"
vg_high_to_low="//android.widget.ScrollView[@content-desc='Selector container']/android.view.ViewGroup/android.view.ViewGroup[@index='4']"
vg_add_to_cart="//android.view.ViewGroup[@content-desc='test-Item' and @index='0']/android.view.ViewGroup/android.view.ViewGroup[@content-desc='test-ADD TO CART']"
btn_cart="//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
txt_title_yourcart="//android.view.ViewGroup/android.view.ViewGroup[@index='1']/android.widget.TextView[@text='YOUR CART']"
btn_checkout="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[@content-desc='test-CHECKOUT']"


#checkout information page locators
txt_firstname="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[@text='First Name']"
txt_lastname="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[@text='Last Name']"
txt_postalcode="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[@text='Zip/Postal Code']"
btn_continue="//android.widget.ScrollView[@content-desc='test-Checkout: Your Info']/android.view.ViewGroup/android.view.ViewGroup[@index='8']"

#checkout overview page locators
txt_checkout_overview="//android.view.ViewGroup/android.view.ViewGroup[@index='1']/android.widget.TextView[@text='CHECKOUT: OVERVIEW']"
btn_finish="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[@index='14']"

#checkout complete page locators
txt_checkout_complete="//android.view.ViewGroup/android.view.ViewGroup[@index='1']/android.widget.TextView[@text='CHECKOUT: COMPLETE!']"