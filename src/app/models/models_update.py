from time import tzname
from typing import Optional
from odmantic.bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime, time, timedelta,timezone
from typing import Collection, List, Optional, Union
from datetime import date, datetime, timezone
from odmantic import AIOEngine, Model, ObjectId,Reference, Field, model
from starlette.requests import cookie_parser

from app.models.models import description




class Merchant_product_details_update(Model):
    active :Optional[int]
    merchant_product_id : Optional[int]
    sku : Optional[str]
    retail_price :Optional[str] 
    total_cost : Optional[str]
    reference_no : Optional[str]
    # updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str] 

class Partner_category_details_update(Model):
    active :int
    partner_category :  Optional[str]
    partner_category_id :  Optional[str]
    partner_category_name : Optional[str]
    partner_sub_category: Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs :  Optional[str] 

    # class Config:
    #     collection = "Partner_category"
class language_update(Model):
    active :Optional[int] 
    language : Optional[str]
    language_code : Optional[str]   
    User_access_logs : Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow) 

class redemption_method_update(Model):
    active :Optional[int] 
    redemption_method : Optional[str]
    redemption_method_id : Optional[str]   
    User_access_logs : Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow) 


class activation_required_update(Model):
    active :Optional[int] 
    activation_required : Optional[str]
    activation_required_id : Optional[str]   
    User_access_logs : Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow) 

class tags_update(Model):
    active :Optional[int] 
    tags : Optional[str]
    tags_id : Optional[str] 
    tags_category : Optional[str]  
    User_access_logs : Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow) 

class description_update(Model):
    active :Optional[int] 
    description : Optional[str]
    description_id : Optional[str]   
    User_access_logs : Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow) 

class documentation_update(Model):
    active :Optional[int] 
    documentation : Optional[str]
    documentation_id : Optional[str]   
    User_access_logs : Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow) 

class product_category_update(Model):
    active :Optional[int]
    product_category : Optional[str]
    product_category_id :Optional[str]
    product_sub_category:Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class organization_update(Model):
    active :Optional[int]
    organization : Optional[str]
    organization_id : Optional[str]    
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class giftcard_prefix_update(Model):
    active :Optional[int]
    giftcard_prefix : Optional[str]
    giftcard_prefix_id : Optional[str]
    giftcard_prefix_name : Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class weight_update(Model):
    active :Optional[int]
    weight : Optional[str]
    weight_id : Optional[str]    
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class shipping_cost_update(Model):
    active :Optional[int]
    shipping_cost : Optional[str]
    shipping_cost : Optional[str]   
    shipping_provider : Optional[str] 
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class warranty_update(Model):
    active :Optional[int]
    warranty : Optional[str]
    warranty_id : Optional[str]    
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class select_colors_update(Model):
    active :Optional[int]
    select_colors : Optional[str]
    select_colors_id : Optional[str]    
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class mapping_for_update(Model):
    active :Optional[int]
    mapping_for : Optional[str]
    mapping_for_id : Optional[str]    
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class sales_update(Model):
    active :Optional[int]
    sales : Optional[str]
    sales_id : Optional[str]    
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

class vat_update(Model):
    active :Optional[int]
    vat : Optional[str]
    vat_id : Optional[str]    
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : Optional[str]

# class overview_update(Model):
#     active :Optional[int]
#     overview : Optional[str]
#     overview_id : Optional[str]    
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at :  datetime = Field(default_factory=datetime.utcnow)
#     User_access_logs : Optional[str]

class gift_card_length_update(Model):
    active :Optional[int] 
    gift_card_length : Optional[int]
    User_access_logs : Optional[str]
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
# class User_access_logs(Model):
#     version : int
#     user_id : int
#     login_timestamp :  datetime
#     ip_address : str 
#     whitelisted_proxy_flag : int
#     failed_login_attempt_flag : int
#     tracker_cookie : int
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime = Field(default_factory=datetime.utcnow)

#     class Config:
#         collection = "user_access_logs"
#         arbitrary_types_allowed = True


class giftcard_attribute_values_update(Model):
    version : Optional[int]
    giftcard_details_id :Optional[int]
    attribute_id :Optional[int]
    attribute_value :Optional[str]
    # updated_at :datetime = Field(default_factory=datetime.utcnow)


# class administrators(Model):
#     version : int
#     active : bool
#     first_name : str
#     last_name : str
#     email :str
#     encrypted_password :str
#     system_account_flag : bool
#     invitation_token : str
#     invitation_created_at : datetime = Field(default_factory=datetime.utcnow)
#     invitation_accepted_at : datetime = Field(default_factory=datetime.utcnow)
#     reset_password_token : str
#     reset_password_sent_at :str
#     remember_created_at : datetime
#     modified_by : int
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime = Field(default_factory=datetime.utcnow)
#     super_admin_flag : int

#     class Config:
#         collection = "administrators"
#         arbitrary_types_allowed = True

class merchant_product_orders_update(Model):
    order_status : Optional[str]
    user_id: Optional[int]
    user_address_id: Optional[int]
    order_total : Optional[float]
    orderid :Optional[str]
    payment_refno : Optional[str]
    payment_message : Optional[str]
    payment_fee : Optional[float]
    current_exchange_rate : Optional[float]
    language_code : Optional[str]
    order_message : Optional[str]
    payment_session_id : Optional[str]
    amount_paid_in_sar : Optional[str]
    points : Optional[str]
    
    # updated_at : datetime = Field(default_factory=datetime.utcnow)
    is_gift : Optional[bool]
    shipment_tracking_id :Optional[str]
    payment_method_id : Optional[int]
    shipment_tracking_url : Optional[str]
    # shipment_date : Optional[datetime] = Field(default_factory=datetime.utcnow)
    price_in_points : Optional[int]


class brand_categories_update(Model):
    version: Optional[int]
    brand_id : Optional[str]
    category_id : Optional[str]
    category_name : Optional[str]
    primary_category_flag : Optional[int]
    modified_by : Optional[str]
    
    # updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)



# class user_activity_logs(Model):
#     version : int
#     activity_name : str
#     customer_id : str
#     ip_address : str
#     status : str
#     brand_id : int
#     user_orderid : str
#     description : str
#     activity_starts_at : datetime = Field(default_factory=datetime.utcnow)
#     activity_ends_at : datetime = Field(default_factory=datetime.utcnow)
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime = Field(default_factory=datetime.utcnow)

#     class Config:
#         collection = "user_activity_logs"
#         arbitrary_types_allowed = True


class brand_category_transaction_categories_update(Model):
    version : Optional[int]
    brand_category_id : Optional[ObjectId]
    transaction_category_id : Optional[ObjectId]
    default_transaction_category_flag :Optional[int]
    modified_by : Optional[int]
   
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)


class user_order_details_update(Model):
    version : Optional[int]
    order_details_status: Optional[str]
    order_id: Optional[int]
    giftcard_variety_id : Optional[int]
    giftcard_style_id : Optional[int]
    delivery_method_id : Optional[int]
    giftcard_value : Optional[float]
    quantity : Optional[int]
    reward_points : Optional[int]
    distributor_reserved_flag : Optional[str]

    # updated_at: datetime = Field(default_factory=datetime.utcnow)
    user_credits : Optional[int]
    rate : Optional[float]
    points : Optional[int]
    mobile_number : Optional[str]
    topup_destination : Optional[str]
    mobile_operator : Optional[str]
    topup_value : Optional[str]
    topup_product_id : Optional[str]
    topup_currency : Optional[str]
    recharge_type : Optional[str]



class merchant_product_detail_variant_values_update(Model):
    active : Optional[bool]
    merchant_product_detail_id : Optional[ObjectId]
    variant_id : Optional[int]
    variant_value_id : Optional[ObjectId]
    reference_no : Optional[str] 
  
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)


class brand_images_update(Model):
    brand_id :Optional[ObjectId]
    image : Optional[str]
    name : Optional[str]
    default_image_flag : Optional[int]
    image_processing : Optional[int]
   
    # updated_at : datetime = Field(default_factory=datetime.utcnow)



# class user_logins(Model):
#     version : int
#     active : bool
#     user_id : int
#     normalized_email : str
#     reset_password_token : str
#     reset_password_sent_at : datetime = Field(default_factory=datetime.utcnow)
#     reset_password_token_expires_at : datetime = Field(default_factory=datetime.utcnow)
#     password_reset_at : datetime = Field(default_factory=datetime.utcnow)
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime = Field(default_factory=datetime.utcnow)

#     class Config:
#         collection = "user_logins"
#         arbitrary_types_allowed = True


class giftcard_batches_update(Model):
    version : Optional[int]
    batch_status :Optional[str]
 
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
    batchid : Optional[str] 
    supplier_orderid : Optional[str]
    supplier_account_id : Optional[int]


class giftcard_variety_brands_update(Model):
    version : Optional[int]
    giftcard_variety_id : Optional[int]
    brand_id : Optional[ObjectId]
    primary_flag : Optional[int]
    modified_by: Optional[int]

    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)


class merchant_product_order_details_update(Model):
    version : Optional[int]
    order_details_status : Optional[str]
    merchant_product_order_id : Optional[int]
    merchant_product_id : Optional[int]
    product_value : Optional[float]
    quantity : Optional[int]
  
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
    merchant_product_detail_id : Optional[int]


class experience_order_details_update(Model):
    experience_order_id : Optional[int]
    giftcard_variety_id : Optional[int]
    order_detail_status: Optional[str]
    experience_value : Optional[float]
    number_of_users : Optional[int]
    # slot_date : Optional[datetime] = Field(default_factory=datetime.utcnow)
    # slot_time : Optional[datetime] = Field(default_factory=datetime.utcnow)
   
    # updated_at :Optional[datetime] = Field(default_factory=datetime.utcnow)
    confirmation_code: Optional[str]
    confirmation_message : Optional[str]
    experience_code_id : Optional[str]
    experience_url: Optional[str]


class homepage_banners_update(Model):
    version : Optional[int]
    active : Optional[bool]
    banner : Optional[str]
    banner_arabic : Optional[str]
    banner_clickable_flag : Optional[str]
    brand_id : Optional[int]
 
    # updated_at : datetime = Field(default_factory=datetime.utcnow)
    sort_order : Optional[int]


class point_transactions_update(Model):
    version : Optional[int]
    user_id : Optional[ObjectId]
    user_order_id : Optional[ObjectId]
    points : Optional[int]
    transaction_type : Optional[str]
    # transaction_timestamp : Optional[datetime] = Field(default_factory=datetime.utcnow)
    exchange_rate : Optional[float]
    
    # updated_at :Optional[datetime] = Field(default_factory=datetime.utcnow)
    merchant_product_order_id : Optional[ObjectId]
    offer_order_id : Optional[ObjectId]
    experience_order_id : Optional[ObjectId]


class offer_campaign_images_update(Model):
    offer_campaign_id : Optional[ObjectId]
    image : Optional[str]
    default_image_flag : Optional[int]
    
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)



# class user_payment_methods(Model):
#     version : int
#     payment_method_name : str
#     active : bool
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime =  Field(default_factory=datetime.utcnow)
#     payment_method_type : str
#     wallet_flag : int
#     payment_fee_rate : float
#     enable_payment_fee_rate : int

#     class Config:
#         collection = "user_payment_methods"
#         arbitrary_types_allowed = True


class giftcard_units_update(Model):
    version : Optional[int]
    unit_name : Optional[str]
    unit_name_short : Optional[str]
    unit_symbol : Optional[str]
    unit_type : Optional[str]
    active : Optional[bool]
    fractional_value_permitted_flag : Optional[int]
    underlying_unit_id : Optional[int]
    underlying_rate : Optional[int]
    modified_by : Optional[int]
    
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
    current_exchange_rate : Optional[float]
    # exchange_rate_update_timestamp : Optional[datetime] = Field(default_factory=datetime.utcnow)
    unit_name_arabic : Optional[str]
    country_id : Optional[int] 


class merchant_product_categories_update(Model):
    active : Optional[bool]
    merchant_product_id : Optional[ObjectId]
    category_id: Optional[int]
    
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)



class offer_campaigns_update(Model):
    version : Optional[int]
    active : Optional[bool]
    is_featured : Optional[bool]
    brand_id :Optional[ObjectId]
    giftcard_unit_id : Optional[int]
    title : Optional[str]
    title_arabic : Optional[str]
    offer_detail : Optional[str]
    offer_detail_arabic : Optional[str]
    value : Optional[int]
    discount : Optional[int]
    estimate_saving : Optional[int]
    redemption_limit : Optional[int]
    # effective_from_date : Optional[datetime] = Field(default_factory=datetime.utcnow)
    # effective_to_date : Optional[datetime] = Field(default_factory=datetime.utcnow)

    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
    product_id : Optional[str]
    sort_order : Optional[float]
    reference_no : Optional[str]
    offer_value : Optional[int]

class openid_providers_update(Model):
    version : Optional[int]
    provider_name : Optional[str]
    active : Optional[bool]
    secure_messaging_flag : Optional[bool]
    contact_cache_hours: Optional[bool]
    provider_priority : Optional[float]
    confirmed_contact_provider_flag : Optional[int]
    
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)


# class administrator_access_logs(Model):
#     version : int
#     administrator_id : int
#     login_timestamp : datetime
#     ip_address : str
#     failed_login_attempt_flag : bool
#     tracker_cookie : str
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime = Field(default_factory=datetime.utcnow)

#     class Config:
#         collection = "administrator_access_logs"
#         arbitrary_types_allowed = True


class wallet_giftcards_update(Model):
    version : Optional[int]
    wallet_id :Optional [int]
    giftcard_id : Optional[ObjectId]
    notified_flag : Optional[bool]
   
    # updated_at : Optional[datetime] = Field(default_factory=datetime.utcnow)


class delivery_methods_update(Model):
    version : Optional[int]
    delivery_method_name : Optional[str]
    active : Optional[bool]
    electronic_delivery_flag : Optional[bool]
    
    # updated_at : datetime = Field(default_factory=datetime.utcnow)



# class roles(Model):
#     version : int
#     role_name : str
#     active : bool
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime = Field(default_factory=datetime.utcnow)

#     class Config:
#         collection = "roles"
#         arbitrary_types_allowed = True


# class supplier_accounts_update(Model):
#     version : Optional[int]
#     active : Optional[bool]
#     first_name : Optional[str]
#     last_name : Optional[str]
#     email : Optional[str]
#     encrypted_password : Optional[str]
#     service_account_flag : Optional[bool]
#     supplier_id : Optional[ObjectId]
#     invitation_token : Optional[str]
#     # invitation_created_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
#     # invitation_accepted_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
#     reset_password_token : Optional[str]
#     # reset_password_sent_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
#     # remember_created_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
#     modified_by : Optional[str]
    
#     # updated_at : datetime = Field(default_factory=datetime.utcnow)


class merchant_product_images_update(Model):
    merchant_product_id : Optional[ObjectId]
    image : Optional[str]
    default_image_flag : Optional[bool]
    
    # updated_at : datetime = Field(default_factory=datetime.utcnow)



class wallets_update(Model):
    version : Optional[int]
    wallet_type : Optional[str]
    user_id : Optional[ObjectId]
    sharing_connection_id : Optional[ObjectId]
    wallet_name : Optional[str]
    color : Optional[str]
    giftcards_count: Optional[str]
    non_zero_balance_giftcards_count : Optional[int]
    
    # updated_at : datetime = Field(default_factory=datetime.utcnow)



class whitelisted_proxies_update(Model):
    version : Optional[int]
    active : Optional[bool]
    ip_address : Optional[str]
    proxy_comment: Optional[str]
    # added_timestamp : Optional[datetime] = Field(default_factory=datetime.utcnow)
    modified_by : Optional[ObjectId]

    # updated_at :datetime = Field(default_factory=datetime.utcnow)


class third_party_brands_update(Model):
    version : Optional[int]
    active : Optional[bool]
    provider : Optional[str]
    flex_init_amount_flag : Optional[bool]
    third_party_brand_name : Optional[str]
    third_party_brand_id : Optional[int]
    brand_id : Optional[ObjectId]
    giftcard_variety_id : Optional[ObjectId]

    # updated_at : datetime = Field(default_factory=datetime.utcnow)
    giftcard_margin_rate : Optional[float]
    giftcard_unit_id : Optional[ObjectId]
    campaign_id : Optional[str]
    sku : Optional[str]
    
    
class giftcard_types_update(Model):
    version : Optional[int]
    giftcard_type_name : Optional[str]
    active : Optional[bool]
    modified_by : Optional[ObjectId]
 
    # updated_at : datetime

class experience_orders_update(Model):
    user_id : Optional[ObjectId]
    order_status : Optional[str]
    order_total : Optional[float]
    orderid : Optional[str]
    language_code : Optional[str]
    points : Optional[int]
    payment_method_id : Optional[ObjectId]
    payment_session_id : Optional[ObjectId]
    payment_refno : Optional[str]
    payment_fee : Optional[float]
    current_exchange_rate : Optional[float]
    amount_paid_in_sar : Optional[float]
    order_message : Optional[str]
   
    # updated_at : datetime


class suppliers_update(Model):
    version : Optional[int]
    supplier_name :Optional[str]
    active : Optional[bool]
    payment_threshold_amount : Optional[float]
    payment_hold_days : Optional[int]
    supplier_group_id :Optional[ObjectId]
    supplier_priority : Optional[float]
    supplier_same_rate_priority : Optional[float]
    supplier_info_verification : Optional[str]
    supplier_referred_by : Optional[str]
    supplier_notes : Optional[str]
    modified_by : Optional[ObjectId]
   
    # updated_at : Optional[datetime]
#######
class partner_update(Model):
    version : int
    active :int
    birthday : Optional[datetime]
    contact_no : Optional[str]
    created_at : Optional[datetime]
    customer_id : Optional[str]
    default_currency_id : Optional[ObjectId]
    email : Optional[str]
    encrypted_password : Optional[str]
    first_name : Optional[str]
    gender : Optional[str]
    last_name : Optional[str]
    modified_by : Optional[ObjectId]
    partner_category_id : Optional[str]
    partner_id : Optional[str]
    partner_info_verification : Optional[str]
    partner_name :Optional[str]
    partner_notes : Optional[str]
    partner_priority : Optional[float]
    partner_referred_by : Optional[str]
    partner_same_rate_priority : Optional[float]
    partner_status : Optional[str]
    password_reset_required_flag : Optional[bool]
    payment_hold_days : Optional[int]
    payment_threshold_amount : Optional[float]
    point_balance : Optional[ObjectId]
    show_empty_wallets_flag : Optional[bool]
    show_zero_balance_giftcards_flag : Optional[bool]
    sync_birthday_flag : Optional[bool]
    sync_first_name_flag : Optional[bool]
    sync_gender_flag : Optional[bool]
    sync_last_name_flag : Optional[bool]
    updated_at : Optional[datetime]
    invitation_token : Optional[str]
    service_account_flag : Optional[bool]
    invitation_created_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
    invitation_accepted_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
    reset_password_sent_at : Optional[datetime]= Field(default_factory=datetime.utcnow)
    remember_created_at : Optional[datetime] = Field(default_factory=datetime.utcnow)
    modified_by : Optional[str]
    partner_group_id :Optional[ObjectId]


    class Config:
        collection = "partner"
#         arbitrary_types_allowed = True

########    
class supplier_access_logs_update(Model):
    version : Optional[int]
    supplier_account_id : Optional[ObjectId]
    # login_timestamp : Optional[datetime]
    ip_address : Optional[str]
    failed_login_attempt_flag : Optional[int]
    tracker_cookie : Optional[str]

    # updated_at : datetime

class offer_campaign_categories_update(Model):
    active : Optional[bool]
    offer_campaign_id : Optional[ObjectId]
    category_id : Optional[ObjectId]
   
    # updated_at :Optional[datetime]


class giftcards_update(Model):
    version : Optional[int]
    giftcard_style_id : Optional[ObjectId]
    user_id : Optional[ObjectId]
    giftcard_key : Optional[str]
    giftcard_source : Optional[str]
    giftcard_status : Optional[str]
    value_source : Optional[str]
    giftcard_number : Optional[str]
    giftcard_pin : Optional[str]
    reloadable_giftcard_id : Optional[str]
    supplier_id : Optional[str]
    organization_id :Optional[str]
    brand_id : Optional[str]
    brand_category_id :Optional[str ]
    giftcard_length_id :Optional[str]
    giftcard_prefix_id :Optional[str]
    redemption_method_id :Optional[str]
    activation_required_id :Optional[str]
    partner_id : Optional[str]
    description_id : Optional[str]
    giftcard_variant_id: Optional[str]
    giftcard_attribute_id : Optional[str]
    giftcard_image_id : Optional[str]
    giftcard_thumbnail_id : Optional[str]
    language_id: Optional[str]
    country_id :  Optional[str]
    tags_id :  Optional[str]
    giftcard_denomination_id : Optional[str]
    giftcard_style_images_id : Optional[str]
    giftcard_type_id: Optional[str]
    giftcard_term_id: Optional[str]
    key_benefits : Optional[str]
    start_date : Optional[datetime]
    expiration_date : Optional[datetime]
    original_value : Optional[float]
    remaining_value : Optional[float]
    number_revealed_flag : Optional[bool]
    multipack_flag :Optional[bool]
    
    # updated_at :datetime
    active :Optional[bool]
    ehadaya_card_flag : Optional[bool]
    custom_giftcard_flag : Optional[bool]
    giftcard_link : Optional[str]
    giftcard_token : Optional[str]
    third_party_giftcard_url : Optional[str]
    giftcard_access_key : Optional[str]
    pkpass_link : Optional[str]
    paper_voucher_flag : Optional[bool]
    giftcard_request_id : Optional[str]


class giftcard_terms_update(Model):
    version: Optional[int]
    giftcard_variety_id : Optional[int]
    # effective_from_date : Optional[datetime]
    # effective_to_date : Optional[datetime]
    # retrieved_timestamp :Optional[datetime]
    terms_url : Optional[str]
    terms_text : Optional[str]
    modified_by : Optional[ObjectId]
    sort_order : Optional[float]
    
    # updated_at : datetime
    language : Optional[str]



class experience_details_update(Model):
    giftcard_variety_id : Optional[ObjectId]
    experience_detail : Optional[str]
    experience_detail_arabic : Optional[str]
    cancellation_policy : Optional[str]
    cancellation_policy_arabic : Optional[str]
    whats_included : Optional[str]
    whats_included_arabic : Optional[str]
    
    # updated_at : datetime



class experience_slots_update(Model):
    active : Optional[bool]
    giftcard_variety_id : Optional[ObjectId]
    # slot_date : Optional[datetime]
    # slot_time : Optional[datetime]

    # updated_at : datetime


class experience_order_recipients_update(Model):
    name : Optional[str]
    email : Optional[str]
    phone_number : Optional[str]

    # updated_at :datetime
    experience_order_detail_id : Optional[ObjectId]

class giftcard_styles_update(Model):
    version : Optional[int]
    style_name : Optional[str]
    style_description : Optional[str]
    default_style_flag : Optional[bool]
    giftcard_variety_id : Optional[ObjectId]
    modified_by : Optional[ObjectId]
    
    # updated_at :datetime
    variety_specific_flag :Optional[bool]
    sort_order : Optional[float]
    style_description_arabic :Optional[str]


class experience_images_update(Model):
    active : Optional[bool]
    image : Optional[str]
    default_image_flag : Optional[bool]
    giftcard_variety_id : Optional[bool]
    # created_at : Optional[datetime]
    # updated_at : datetime
    sort_order : Optional[float]

class variants_update(Model):
    active : Optional[bool]
    variant_name : Optional[str]
    variant_code : Optional[str]

    # updated_at : datetime
    variant_name_arabic : Optional[str]


class user_phones_update(Model):
    version : Optional[int]
    active : Optional[bool]
    user_id : Optional[ObjectId]
    phone : Optional[str]
    default_phone_flag : Optional[bool]
    verified_phone_flag : Optional[bool]
    verification_code : Optional[str]
    # verification_code_sent_at : Optional[datetime]
    # verification_code_expires_at : Optional[datetime]
    # phone_verified_at : Optional[datetime]
    
    # updated_at : datetime


class giftcard_attributes_update(Model):
    version : Optional[int]
    attribute_name : Optional[str]
    validation_pattern_id : Optional[ObjectId]
    attribute_value : Optional[str]
    modified_by : Optional[ObjectId]
    
    # updated_at : datetime


class experience_prices_update(Model):
    active : Optional[bool]
    giftcard_variety_id : Optional[bool]
    number_of_users : Optional[bool]
    price : Optional[float]
    shipping_cost : Optional[float]
    sales_tax : Optional[float]
    vat : Optional[float]
    total_cost : Optional[float]
    
    # updated_at : datetime


class brands_update(Model):
    version : Optional[int]
    active : Optional[bool]
    display_name : Optional[str]
    sort_name : Optional[str]
    brand_url : Optional[str]
    store_locator_url : Optional[str]
    affiliate_url : Optional[str]
    copyright_notice : Optional[str]
    custom_brand_flag : Optional[bool]
    user_id : Optional[ObjectId]
    default_transaction_category_id : Optional[ObjectId]
    modified_by : Optional[ObjectId]
    sort_order : Optional[float]
   
    # updated_at : datetime
    brand_reference_no : Optional[str]
    distributor_id : Optional[ObjectId]
    featured_flag : Optional[bool]
    display_name_arabic : Optional[str]
    is_topup : Optional[bool]
    point_exchange_flag : Optional[bool]



# class administrator_roles(Model):
#     version : ObjectId
#     administrator_id : ObjectId
#     role_id : ObjectId
#     modified_by : ObjectId
#     created_at :datetime
#     updated_at :datetime

#     class Config:
#         collection = "administrator_roles"
#         arbitrary_types_allowed = True


class offer_campaign_terms_update(Model):
    offer_campaign_id : Optional[ObjectId]
    terms_text :Optional[str]
    language : Optional[str]
 
    # updated_at :datetime



class interface_methods_update(Model):
    version : Optional[int]
    method_name : Optional[str]
    active : Optional[bool]
    physical_card_required_flag : Optional[bool]
    method_type : Optional[str]
    # created_at : Optional[str]
    # updated_at : Optional[str]

class merchant_product_transaction_categories_update(Model):
    active : Optional[bool]
    merchant_product_id : Optional[ObjectId]
    transaction_category_id : Optional[ObjectId]

    # updated_at : datetime

class giftcard_denominations_update(Model):
    version : Optional[int]
    denomination_value : Optional[float]
    active : Optional[bool]
    modified_by : Optional[ObjectId]
    # updated_at :datetime


class gifts_update(Model):
    version : Optional[int]
    gift_status : Optional[str]
    communication_method : Optional[str]
    giftcard_id : Optional[ObjectId]
    sender_id : Optional[ObjectId]
    recipient_id : Optional[ObjectId]
    user_order_detail_id : Optional[ObjectId]
    provider_id : Optional[ObjectId]
    provider_uid : Optional[str]
    recipient_phone : Optional[str]
    recipient_email : Optional[str]
    recipient_first_name : Optional[str]
    recipient_last_name : Optional[str]
    sender_first_name : Optional[str]
    sender_last_name : Optional[str]
    access_pin : Optional[str]
    message : Optional[str]
    consecutive_failed_access_attempt_count : Optional[bool]
    delivery_attempt_count : Optional[int]
    # scheduled_delivery_date : Optional[datetime]
    sender_notified_flag : Optional[bool]
    recipient_notified_flag : Optional[bool]
    claim_token : Optional[str]
  
    # updated_at :datetime
    # delivered_at :Optional[datetime]

class merchant_product_variants_update(Model):
    active : Optional[bool]
    merchant_product_id : Optional[ObjectId]
    variant_id : Optional[ObjectId]
  
    # updated_at :Optional[datetime]

class user_order_details_giftcards_update(Model):
    version : Optional[int]
    order_details_id : Optional[ObjectId]
    giftcard_details_id : Optional[ObjectId]
    modified_by : Optional[ObjectId]
   
    # updated_at : datetime


# class user_tokens(Model):
#     version : ObjectId
#     active : bool
#     user_id : ObjectId
#     user_login_id : ObjectId
#     user_phone_login_id : ObjectId
#     user_openid_id : ObjectId
#     user_agent : str
#     login_type : str
#     perishable_token : str
#     token_expires_at : datetime
#     created_at :datetime
#     updated_at :datetime

#     class Config:
#         collection = "user_tokens"
#         arbitrary_types_allowed = True
    

class user_addresses_update(Model):
    version : Optional[int]
    active : Optional[bool]
    user_id : Optional[ObjectId]
    normalized_address_id : Optional[ObjectId]
    address_street1 : Optional[str]
    address_street2 : Optional[str]
    address_city : Optional[str]
    address_state : Optional[str]
    address_country : Optional[str]
    zip_code: Optional[str]
    phone_number : Optional[str]
    preferred_flag : Optional[bool]
    notified_flag : Optional[bool]
    validated_flag : Optional[bool]
  
    # updated_at : datetime
    first_name : Optional[str]
    last_name : Optional[str]
    email : Optional[str]
    mobile_number : Optional[str]
    company_name : Optional[str]


# class user_credit_cards_update(Model):
#     version : ObjectId
#     user_id : ObjectId
#     user_payment_method_id : ObjectId
#     billing_address_id : ObjectId
#     credit_card_type : str
#     credit_card_number : str
#     credit_card_expiration_month : str
#     credit_card_expiration_year : str
#     notified_flag : bool
#     billing_address_verified_flag : bool
#     created_at : datetime
#     updated_at :datetime

#     class Config:
#         collection = "user_credit_cards"
#         arbitrary_types_allowed = True


class countries_update(Model):
    country_name : Optional[str]
    country_code : Optional[str]
    region : Optional[str]
    subregion: Optional[str]
 
    # updated_at : Optional[datetime]
    country_name_arabic : Optional[str]
    

class categories_update(Model):
    version : Optional[int]
    category_name : Optional[str]
    active : Optional[bool]
    sort_order : Optional[float]
    modified_by : Optional[ObjectId]
   
    # updated_at :Optional[datetime]
    category_type : Optional[str]
    category_image : Optional[str]
    banner : Optional[str]
    banner_arabic : Optional[str]
    category_name_arabic :Optional[str]



class redemption_partners_update(Model):
    version : Optional[int]
    active : Optional[bool]
    partner_name : Optional[str]
    partner_name_arabic : Optional[str]
    country_id : Optional[ObjectId]
    partner_logo: Optional[str]

    # updated_at : Optional[datetime]

class user_openids_update(Model):
    version : Optional[int]
    user_id : Optional[ObjectId]
    provider_id : Optional[ObjectId]
    provider_uid : Optional[str]
    identifier_url : Optional[str]
    name : Optional[str]
    email : Optional[str]
    verified_email: Optional[str]
    avatar_url : Optional[str]
    access_token : Optional[str]
    # expires_at :Optional[datetime]
    gender : Optional[str]
    # birthday : Optional[datetime]
    default_openid_flag : Optional[bool]
    notified_flag : Optional[bool]

    # updated_at : Optional[datetime]


# class user_phone_logins_update(Model):
#     version : ObjectId
#     active : bool
#     user_id : ObjectId
#     normalized_phone : str
#     reset_password_token : str
#     reset_password_sent_at : datetime
#     reset_password_token_expires_at : datetime
#     password_reset_at : datetime
#     created_at : datetime
#     updated_at : datetime

#     class Config:
#         collection = "user_phone_logins"
#         arbitrary_types_allowed = True


class transaction_categories_update(Model):
    version : Optional[int]
    category_name : Optional[str]
    active : Optional[bool]
    private_category_flag : Optional[bool]
    user_id : Optional[ObjectId]
    
    # updated_at : Optional[datetime]


class giftcard_variety_denominations_update(Model):
    version : Optional[int]
    active : Optional[bool]
    giftcard_variety_id : Optional[ObjectId]
    giftcard_denomination_id : Optional[ObjectId]
    modified_by : Optional[ObjectId]

    # updated_at :Optional[datetime]

class giftcard_details_update(Model):
    version : Optional[int]
    giftcard_id : Optional[ObjectId]
    giftcard_variety_id : Optional[ObjectId]
    delivery_method_id : Optional[ObjectId]
    distributor_id : Optional[ObjectId]
    multipack_quantity : Optional[bool]
    # issued_date : Optional[datetime]

    # updated_at : Optional[datetime]


class third_party_order_details_update(Model):
    delivery_method_id : Optional[ObjectId]
    third_party_order_id : Optional[ObjectId]
    giftcard_variety_id : Optional[ObjectId]
    card_number : Optional[str]
    # expiration_date :Optional[datetime]
    original_value :Optional[float]
    remaining_value : Optional[float]
    card_pin : Optional[str]
    order_detail_status : Optional[str]
   
    # updated_at : Optional[datetime]
    giftcard_detail_id : Optional[ObjectId]
    giftcard_margin_rate: Optional[float]
    card_url : Optional[str]
    card_access_key : Optional[str]


class user_orders_update(Model):
    version : Optional[int]
    order_status : Optional[str]
    user_id : Optional[ObjectId]
    payment_method_id : Optional[ObjectId]
    shipping_address_id : Optional[ObjectId]
    distributor_transaction_id : Optional[ObjectId]
    reward_program_transaction_id : Optional[ObjectId]
    order_total : Optional[float]
    orderid : Optional[str]
    payment_refno : Optional[str]
    payment_message : Optional[str]
   
    # updated_at : Optional[datetime]
    total_amount : Optional[float]
    order_type : Optional[str]
    user_distributor_transaction_id : Optional[ObjectId]
    payment_fee : Optional[float]
    current_exchange_rate :Optional[float]
    language_code : Optional[str]
    order_message : Optional[str]
    payment_session_id : Optional[str]
    amount_paid_in_sar : Optional[float]
    points_exchange_member_id : Optional[str]
    points : Optional[ObjectId]
    converted_points : Optional[ObjectId]



class offer_order_details_update(Model):
    version : Optional[int]
    order_details_status: Optional[str]
    offer_order_id : Optional[ObjectId]
    offer_campaign_id : Optional[ObjectId]
    offer_value : Optional[float]
    quantity : Optional[ObjectId]
    
    # updated_at : Optional[datetime]
    store_name : Optional[str]
    gift_message : Optional[str]
    recipient_email : Optional[str]
    recipient_phone : Optional[str]


class giftcard_batch_giftcard_details_update(Model):
    version : Optional[int]
    giftcard_batch_id : Optional[ObjectId]
    giftcard_details_id : Optional[ObjectId]
    supplier_rate : Optional[int]

    # updated_at : Optional[datetime] 



class giftcard_style_images_update(Model):
    giftcard_style_id : Optional[ObjectId]
    image : Optional[str]
    default_image_flag : Optional[bool]
    image_processing : Optional[bool]

    # updated_at : Optional[datetime]
    banner : Optional[str]
    logo : Optional[str]


class merchant_product_terms_update(Model):
    merchant_product_id : Optional[ObjectId]
    terms_text : Optional[str]
    language : Optional[str]
    
    # updated_at : Optional[datetime]


class merchant_products_update(Model):
    active : Optional[bool]
    brand_id : Optional[ObjectId]
    giftcard_unit_id : Optional[ObjectId]
    product_name : Optional[str]
    product_name_arabic : Optional[str]
    weight : Optional[str]
    sku : Optional[str]
    retail_price : Optional[float]
    shipping_cost : Optional[float]
    sales_tax :Optional[float]
    vat :Optional[float]
    total_cost : Optional[float]
    warranty : Optional[int]
    # expiration_date : Optional[datetime]
    description : Optional[str]
    description_arabic :Optional[str]
   
    # updated_at : Optional[datetime]
    expected_delivery_days : Optional[ObjectId]
    product_id : Optional[str]


class variant_values_update(Model):
    active : Optional[bool]
    variant_id : Optional[ObjectId]
    value_name : Optional[str]
    value_code : Optional[str]
   
    # updated_at : Optional[datetime]
    value_name_arabic: Optional[str]
    color_code : Optional[str]


class offer_orders_update(Model):
    order_status: Optional[str]
    user_id : Optional[ObjectId]
    order_total : Optional[float]
    orderid : Optional[str]
    payment_refno : Optional[str]
    payment_message : Optional[str]
    payment_fee : Optional[float]
    current_exchange_rate : Optional[float]
    language_code : Optional[str]
    order_message : Optional[str]
    payment_session_id : Optional[str]
    amount_paid_in_sar :Optional[float]
    points : Optional[ObjectId]
    # created_at :Optional[datetime]
    # updated_at :Optional[datetime]
    price_in_points : Optional[ObjectId]
    payment_method_id : Optional[ObjectId]
    is_gift : Optional[bool]
    batch_id : Optional[str]
    offer_url : Optional[str]


# class role_entitlements_update(Model):
#     version : ObjectId
#     role_id : ObjectId
#     entitlement_id : ObjectId
#     required_flag : bool
#     default_flag : bool
#     created_at :datetime
#     updated_at :datetime




class giftcard_varieties_update(Model):
    version : Optional[int]
    active : Optional[bool]
    giftcard_type_id : ObjectId
    giftcard_tags_id : ObjectId
    activation_required_flag : Optional[bool]
    no_expiration_flag : Optional[bool]
    validation_required_flag : Optional[bool]
    barcode_required_flag : Optional[bool]
    one_time_use_flag : Optional[bool]
    flex_init_amount_flag : Optional[bool]
    amount :  Optional[int]
    max_init_amount :Optional[float]
    min_init_amount : Optional[float]
    variety_description : Optional[str]
    reloadable_flag : Optional[bool]
    giftcard_denomination_flag : Optional[bool]
    balance_check_url : Optional[str]
    modified_by : Optional[ObjectId]
    # created_at :Optional[datetime]
    # updated_at :Optional[datetime]
    online_flag : Optional[bool]
    offline_flag : Optional[bool]
    online_redemption_instructions :Optional[str]
    offline_redemption_instructions : Optional[str]
    remote_giftcard_url : Optional[str]
    short_description :Optional[str]
    variety_source : Optional[str]
    custom_variety_flag : Optional[bool]
    giftcard_variety_reference_no : Optional[str]
    distributor_id : Optional[ObjectId]
    multilingual_flag : Optional[bool]
    short_description_arabic : Optional[str]



class schema_migrations_update(Model):
    version : Optional[str]


class administrator_activity_logs_update(Model):
    version : Optional[int]
    administrator_id : ObjectId
    ip_address : Optional[str]
    activity_name : Optional[str]
    # activity_starts_at :Optional[datetime]
    # activity_ends_at :Optional[datetime]
    status : Optional[str]
    description: Optional[str]
    entity_name : Optional[str]
    entity_value : Optional[str]
   
    # updated_at :Optional[datetime]



class normalized_addresses_update(Model):
    version : Optional[int]
    avs_address1 : Optional[str]
    avs_address2 : Optional[str]
    avs_phone_number : Optional[str]
   
    # updated_at :datetime


class user_emails_update(Model):
    version : Optional[int]
    user_id : ObjectId
    email : Optional[str]
    normalized_email : Optional[str]
    default_email_flag : Optional[bool]
    verified_email_flag : Optional[bool]
    notified_flag : Optional[bool]
    confirmation_token : Optional[str]
    confirmed_at : Optional[datetime]
    confirmation_sent_at :Optional[datetime]
    confirmation_expires_at :Optional[datetime]
    # updated_at :Optional[datetime]


class offer_campaign_transaction_categories_update(Model):
    active : Optional[bool]
    offer_campaign_id : ObjectId
    transaction_category_id : ObjectId

    # updated_at : datetime

