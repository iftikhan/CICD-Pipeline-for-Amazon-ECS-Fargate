from typing import Collection, List, Optional, Union
from datetime import date, datetime, timezone
from odmantic import AIOEngine, Model, ObjectId,Reference, Field
from pydantic import BaseModel
from starlette.requests import cookie_parser


class Merchant_product_details(Model):
    active :int
    merchant_product_id : int 
    sku : str
    retail_price :str 
    total_cost : str
    reference_no : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

    class Config:
        collection = "merchant_product_details"
#       arbitrary_types_allowed = True

class Partner_category_details(Model):
    active :int
    partner_category : str
    partner_category_id : str
    partner_sub_category:str
    partner_category_name :str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

    class Config:
        collection = "Partner_category"

class language(Model):
    active :int
    language : str
    language_code : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class redemption_method(Model):
    active :int
    redemption_method : str
    redemption_method_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class activation_required(Model):
    active :int
    activation_required : str
    activation_required_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class tags(Model):
    active :int
    tags : str
    tags_id : str
    tags_category : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class description(Model):
    active :int
    description : str
    description_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow) 

class documentation(Model):
    active :int
    documentation : str
    documentation_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str  
  
class gift_card_length(Model):
    active : int
    gift_card_length : int
    User_access_logs : str 
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)

class product_category(Model):
    active :int
    product_category : str
    product_category_id : str
    product_sub_category : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str

class weight(Model):
    active :int
    weight : str
    weight_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class shipping_cost(Model):
    active :int
    shipping_cost : str
    shipping_cost_id : str
    shipping_provider : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class sales(Model):
    active :int
    sales : str
    sales_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class warranty(Model):
    active :int
    warranty : str
    warranty_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class mapping_for(Model):
    active :int
    mapping_for : str
    mapping_for_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str

class select_colors(Model):
    active :int
    select_colors : str
    select_colors_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class vat(Model):
    active :int
    vat : str
    vat_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

# class overview(Model):
#     active :int
#     overview : str
#     overview_id : str
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at :  datetime = Field(default_factory=datetime.utcnow)
#     User_access_logs : str 

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
class organization(Model):
    active :int
    organization : str
    organization_id : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str 

class giftcard_prefix(Model):
    active :int
    giftcard_prefix : str
    giftcard_prefix_id : str
    giftcard_prefix_name : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :  datetime = Field(default_factory=datetime.utcnow)
    User_access_logs : str

class giftcard_attribute_values(Model):
    version : int
    giftcard_details_id :int
    attribute_id :int
    attribute_value :str 
    created_at :datetime = Field(default_factory=datetime.utcnow)
    updated_at :datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "giftcard_attribute_values"
#         arbitrary_types_allowed = True

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

class merchant_product_orders(Model):
    order_status : str
    user_id: int
    user_address_id: int
    order_total : float
    orderid :str
    payment_refno : str
    payment_message : str
    payment_fee : float
    current_exchange_rate : float
    language_code : str
    order_message : str
    payment_session_id : str
    amount_paid_in_sar : str
    points : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)
    is_gift : bool
    shipment_tracking_id :str
    payment_method_id : int
    shipment_tracking_url : str
    shipment_date : datetime = Field(default_factory=datetime.utcnow)
    price_in_points : int

    class Config:
        collection = "merchant_product_orders"
#         arbitrary_types_allowed = True


class brand_categories(Model):
    version: int
    brand_id : str
    category_id : str
    category_name : Optional[str]
    primary_category_flag : int
    modified_by : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "brand_categories"
#         arbitrary_types_allowed = True


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


class brand_category_transaction_categories(Model):
    version : int
    brand_category_id : ObjectId
    transaction_category_id : ObjectId
    default_transaction_category_flag :int
    modified_by : int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "brand_category_transaction_categories"
#       arbitrary_types_allowed = True

class user_order_details(Model):
    version : int
    order_details_status: str
    order_id: int
    giftcard_variety_id : int
    giftcard_style_id : int
    delivery_method_id : int
    giftcard_value : float
    quantity : int
    reward_points : int
    distributor_reserved_flag : str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    user_credits : int
    rate : float
    points : int
    mobile_number : str
    topup_destination : str
    mobile_operator : str
    topup_value : str
    topup_product_id : str
    topup_currency : str
    recharge_type : str

    class Config:
        collection = "user_order_details"
#         arbitrary_types_allowed = True


class merchant_product_detail_variant_values(Model):
    active : bool
    merchant_product_detail_id : ObjectId
    variant_id : ObjectId
    variant_value_id : ObjectId
    reference_no : str 
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config: 
        collection = "merchant_product_detail_variant_values"
#         arbitrary_types_allowed = True


class brand_images(Model):
    brand_id :ObjectId
    image : str
    name : str
    default_image_flag : int
    image_processing : int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "brand_images"
#         arbitrary_types_allowed = True


class user_logins(Model):
    version : int
    active : bool
    user_id : int
    normalized_email : str
    reset_password_token : str
    reset_password_sent_at : datetime = Field(default_factory=datetime.utcnow)
    reset_password_token_expires_at : datetime = Field(default_factory=datetime.utcnow)
    password_reset_at : datetime = Field(default_factory=datetime.utcnow)
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "user_logins"
#         arbitrary_types_allowed = True


class giftcard_batches(Model):
    version : int
    batch_status :str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)
    batchid : str 
    supplier_orderid : str
    supplier_account_id : int

    class Config:
        collection = "giftcard_batches"
#         arbitrary_types_allowed = True

class giftcard_variety_brands(Model):
    version : int
    giftcard_variety_id : int
    brand_id : ObjectId
    primary_flag : int
    modified_by: int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "giftcard_variety_brands"
#         arbitrary_types_allowed = True


class merchant_product_order_details(Model):
    version : int
    order_details_status : str
    merchant_product_order_id : int
    merchant_product_id : int
    product_value : float
    quantity : int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)
    merchant_product_detail_id : int

    class Config:
        collection = "merchant_product_order_details"
#         arbitrary_types_allowed = True


class experience_order_details(Model):
    experience_order_id : int
    giftcard_variety_id : int
    order_detail_status: str
    experience_value : float
    number_of_users : int
    slot_date : datetime = Field(default_factory=datetime.utcnow)
    slot_time : datetime = Field(default_factory=datetime.utcnow)
    created_at :datetime = Field(default_factory=datetime.utcnow)
    updated_at :datetime = Field(default_factory=datetime.utcnow)
    confirmation_code: str
    confirmation_message : str
    experience_code_id : str
    experience_url: str

    class Config:
        collection = "experience_order_details"
#         arbitrary_types_allowed = True


class homepage_banners(Model):
    version : int
    active : bool
    banner : str
    banner_arabic : str
    banner_clickable_flag : str
    brand_id : int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)
    sort_order : int

    class Config:
        collection = "homepage_banners"
#         arbitrary_types_allowed = True


class point_transactions(Model):
    version : ObjectId
    user_id : ObjectId
    user_order_id : ObjectId
    points : int
    transaction_type : str
    transaction_timestamp : datetime = Field(default_factory=datetime.utcnow)
    exchange_rate : float
    created_at :datetime = Field(default_factory=datetime.utcnow)
    updated_at :datetime = Field(default_factory=datetime.utcnow)
    merchant_product_order_id : ObjectId
    offer_order_id : ObjectId
    experience_order_id : ObjectId

    class Config:
        collection = "point_transactions"
#         arbitrary_types_allowed = True


class offer_campaign_images(Model):
    offer_campaign_id : ObjectId
    image : str
    default_image_flag : int
    created_at : datetime =Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "offer_campaign_images"
#         arbitrary_types_allowed = True


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


class giftcard_units(Model):
    version : int
    unit_name : str
    unit_name_short : str
    unit_symbol : str
    unit_type : str
    active : bool
    fractional_value_permitted_flag : int
    underlying_unit_id : int
    underlying_rate : int
    modified_by : int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)
    current_exchange_rate : float
    exchange_rate_update_timestamp : datetime = Field(default_factory=datetime.utcnow)
    unit_name_arabic : str
    country_id : int 

    class Config:
        collection = "giftcard_units"
#       arbitrary_types_allowed = True


class merchant_product_categories(Model):
    active : bool
    merchant_product_id : ObjectId
    category_id: int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "merchant_product_categories"
#         arbitrary_types_allowed = True


class offer_campaigns(Model):
    version : int
    active : bool
    is_featured : bool
    brand_id :ObjectId
    giftcard_unit_id : int
    title : str
    title_arabic : str
    offer_detail : str
    offer_detail_arabic : str
    value : int
    discount : int
    estimate_saving : int
    redemption_limit : int
    effective_from_date : datetime = Field(default_factory=datetime.utcnow)
    effective_to_date : datetime = Field(default_factory=datetime.utcnow)
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)
    product_id : str
    sort_order : float
    reference_no : str
    offer_value : int

    class Config:
        collection = "offer_campaigns"
#         arbitrary_types_allowed = True

class openid_providers(Model):
    version : int
    provider_name : str
    active : bool
    secure_messaging_flag : bool
    contact_cache_hours: bool
    provider_priority : float
    confirmed_contact_provider_flag : int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "openid_providers"
#         arbitrary_types_allowed = True

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


class wallet_giftcards(Model):
    version : int
    wallet_id : int
    giftcard_id : ObjectId
    notified_flag : bool
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "wallet_giftcards"
#         arbitrary_types_allowed = True


class delivery_methods(Model):
    version : int
    delivery_method_name : str
    active : bool
    electronic_delivery_flag : bool
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "delivery_methods"
#         arbitrary_types_allowed = True



# class roles(Model):
#     version : int
#     role_name : str
#     active : bool
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime = Field(default_factory=datetime.utcnow)

#     class Config:
#         collection = "roles"
#         arbitrary_types_allowed = True


# class supplier_accounts(Model):
#     version : int
#     active : bool
#     first_name : str
#     last_name : str
#     email : str
#     encrypted_password : str
#     service_account_flag : bool
#     supplier_id : ObjectId
#     invitation_token : str
#     invitation_created_at : datetime = Field(default_factory=datetime.utcnow)
#     invitation_accepted_at : datetime = Field(default_factory=datetime.utcnow)
#     reset_password_token : str
#     reset_password_sent_at : datetime = Field(default_factory=datetime.utcnow)
#     remember_created_at : datetime = Field(default_factory=datetime.utcnow)
#     modified_by : str
#     created_at : datetime = Field(default_factory=datetime.utcnow)
#     updated_at : datetime = Field(default_factory=datetime.utcnow)

#     class Config:
#         collection = "supplier_accounts"
# #         arbitrary_types_allowed = True



class merchant_product_images(Model):
    merchant_product_id : ObjectId
    image : str
    default_image_flag : bool
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "merchant_product_images"
#         arbitrary_types_allowed = True



class wallets(Model):
    version : int
    wallet_type : str
    user_id : ObjectId
    sharing_connection_id : ObjectId
    wallet_name : str
    color : str
    giftcards_count: str
    non_zero_balance_giftcards_count : int
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "wallets"
#         arbitrary_types_allowed = True


class whitelisted_proxies(Model):
    version : int
    active : bool
    ip_address : str
    proxy_comment: str
    added_timestamp : datetime = Field(default_factory=datetime.utcnow)
    modified_by : ObjectId
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at :datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "whitelisted_proxies"
#         arbitrary_types_allowed = True


class third_party_brands(Model):
    version : int
    active : bool
    provider : str
    flex_init_amount_flag : bool
    third_party_brand_name : str
    third_party_brand_id : int
    brand_id : ObjectId
    giftcard_variety_id : ObjectId
    created_at : datetime
    updated_at : datetime
    giftcard_margin_rate : float
    giftcard_unit_id : ObjectId
    campaign_id : str
    sku : str
    
    class Config:
        collection = "hird_party_brands"
#         arbitrary_types_allowed = True


class giftcard_types(Model):
    version : int
    giftcard_type_name : str
    active : bool
    modified_by : ObjectId
    created_at :datetime
    updated_at : datetime

    class Config:
        collection = "giftcard_types"
#         arbitrary_types_allowed = True



class experience_orders(Model):
    user_id : ObjectId
    order_status : str
    order_total : float
    orderid : str
    language_code : str
    points : int
    payment_method_id : ObjectId
    payment_session_id : ObjectId
    payment_refno : str
    payment_fee : float
    current_exchange_rate : float
    amount_paid_in_sar : float
    order_message : str
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "experience_orders"
#         arbitrary_types_allowed = True


class suppliers(Model):
    version : int
    supplier_name :str
    active : bool
    payment_threshold_amount : float
    payment_hold_days : int
    supplier_group_id :ObjectId
    supplier_priority : float
    supplier_same_rate_priority : float
    supplier_info_verification : str
    supplier_referred_by : str
    supplier_notes : str
    modified_by : ObjectId
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "suppliers"
#         arbitrary_types_allowed = True
#######
class partner(Model):
    version : int
    active :int
    birthday : datetime
    contact_no : str
    created_at : datetime
    customer_id : str
    default_currency_id : ObjectId
    email : str 
    encrypted_password : str
    first_name : str
    gender : str
    last_name : str
    modified_by : ObjectId
    partner_category_id : str
    partner_id : str
    partner_info_verification : str
    partner_name :str
    partner_notes : str
    partner_priority : float
    partner_referred_by : str
    partner_same_rate_priority : float
    partner_status : str
    password_reset_required_flag : bool
    payment_hold_days : int
    payment_threshold_amount : float
    point_balance : ObjectId
    show_empty_wallets_flag : bool
    show_zero_balance_giftcards_flag : bool
    sync_birthday_flag : bool
    sync_first_name_flag : bool
    sync_gender_flag : bool
    sync_last_name_flag : bool
    updated_at : datetime
    invitation_token : str
    service_account_flag : bool
    invitation_created_at : datetime = Field(default_factory=datetime.utcnow)
    invitation_accepted_at : datetime = Field(default_factory=datetime.utcnow)
    reset_password_sent_at : datetime = Field(default_factory=datetime.utcnow)
    remember_created_at : datetime = Field(default_factory=datetime.utcnow)
    modified_by : str
    partner_group_id :ObjectId



    class Config:
        collection = "partner"
#         arbitrary_types_allowed = True
######
class supplier_access_logs(Model):
    version : int
    supplier_account_id : ObjectId
    login_timestamp : datetime
    ip_address : str
    failed_login_attempt_flag : int
    tracker_cookie : str
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "supplier_access_logs"
#         arbitrary_types_allowed = True


class offer_campaign_categories(Model):
    active : bool
    offer_campaign_id : ObjectId
    category_id : ObjectId
    created_at : datetime
    updated_at :datetime

    class Config:
        collection = "offer_campaign_categories"
#         arbitrary_types_allowed = True


class giftcards(Model):
    version : int
    giftcard_style_id : ObjectId
    user_id : ObjectId
    giftcard_key : str
    giftcard_source : str
    giftcard_status : str
    value_source : str
    giftcard_number : str
    giftcard_pin : str
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
    expiration_date : datetime
    original_value : float
    remaining_value : float
    number_revealed_flag : bool
    multipack_flag :bool
    created_at :datetime
    updated_at :datetime
    active :bool
    ehadaya_card_flag : bool
    custom_giftcard_flag : bool
    giftcard_link : str
    giftcard_token : str
    third_party_giftcard_url : str
    giftcard_access_key : str
    pkpass_link : str
    paper_voucher_flag : bool
    giftcard_request_id : str

    class Config:
        collection = "giftcards"
#         arbitrary_types_allowed = True


class giftcard_terms(Model):
    version: int
    giftcard_variety_id : int
    effective_from_date : datetime
    effective_to_date : datetime
    retrieved_timestamp :datetime
    terms_url : str
    terms_text : str
    modified_by : ObjectId
    sort_order : float
    created_at : datetime
    updated_at : datetime
    language : str

    class Config:
        collection = "giftcard_terms"
#         arbitrary_types_allowed = True


class experience_details(Model):
    giftcard_variety_id : ObjectId
    experience_detail : str
    experience_detail_arabic : str
    cancellation_policy : str
    cancellation_policy_arabic : str
    whats_included : str
    whats_included_arabic : str
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "experience_details"
#         arbitrary_types_allowed = True


class experience_slots(Model):
    active : bool
    giftcard_variety_id : ObjectId
    slot_date : datetime
    slot_time : datetime
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "experience_slots"
#         arbitrary_types_allowed = True


class experience_order_recipients(Model):
    name : str
    email : str
    phone_number : str
    created_at : datetime
    updated_at :datetime
    experience_order_detail_id : ObjectId

    class Config:
        collection ="experience_order_recipients"
#         arbitrary_types_allowed = True


class giftcard_styles(Model):
    version : ObjectId
    style_name : str
    style_description : str
    default_style_flag : bool
    giftcard_variety_id : ObjectId
    modified_by : ObjectId
    created_at : datetime
    updated_at :datetime
    variety_specific_flag :bool
    sort_order : float
    style_description_arabic :str

    class Config:
        collection ="giftcard_styles"
#         arbitrary_types_allowed = True
    

class experience_images(Model):
    active : bool
    image : str
    default_image_flag : bool
    giftcard_variety_id : bool
    created_at : datetime
    updated_at : datetime
    sort_order : float

    class Config:
        collection = "experience_images"
#         arbitrary_types_allowed = True


class variants(Model):
    active : bool
    variant_name : str
    variant_code : str
    created_at : datetime
    updated_at : datetime
    variant_name_arabic : str

    class Config:
        collection = "variants"
#         arbitrary_types_allowed = True


class user_phones(Model):
    version : ObjectId
    active : bool
    user_id : ObjectId
    phone : str
    default_phone_flag : bool
    verified_phone_flag : bool
    verification_code : str
    verification_code_sent_at : datetime
    verification_code_expires_at : datetime
    phone_verified_at : datetime
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "user_phones"
#         arbitrary_types_allowed = True



class giftcard_attributes(Model):
    version : ObjectId
    attribute_name : str
    validation_pattern_id : ObjectId
    attribute_value : str
    modified_by : ObjectId
    created_at : datetime
    updated_at : datetime
   
    class Config:
        collection = "giftcard_attributes"
#         arbitrary_types_allowed = True



class experience_prices(Model):
    active : bool
    giftcard_variety_id : bool
    number_of_users : bool
    price : float
    shipping_cost : float
    sales_tax : float
    vat : float
    total_cost : float
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "experience_prices"
#         arbitrary_types_allowed = True


class brands(Model):
    version : ObjectId
    active : bool
    display_name : str
    sort_name : str
    brand_url : str
    store_locator_url : str
    affiliate_url : str
    copyright_notice : str
    custom_brand_flag : bool
    user_id : ObjectId
    default_transaction_category_id : ObjectId
    modified_by : ObjectId
    sort_order : float
    created_at : datetime
    updated_at : datetime
    brand_reference_no : str
    distributor_id : ObjectId
    featured_flag : bool
    display_name_arabic : str
    is_topup : bool
    point_exchange_flag : bool

    class Config:
        collection = "brands"
#         arbitrary_types_allowed = True
    


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


class offer_campaign_terms(Model):
    offer_campaign_id : ObjectId
    terms_text :str
    language : str
    created_at : datetime
    updated_at :datetime

    class Config:
        collection = "offer_campaign_terms"
#         arbitrary_types_allowed = True


class interface_methods(Model):
    version : ObjectId
    method_name : str
    active : bool
    physical_card_required_flag : bool
    method_type : str
    created_at : str
    updated_at : str

    class Config:
        collection ="interface_methods"
#         arbitrary_types_allowed = True

class merchant_product_transaction_categories(Model):
    active : bool
    merchant_product_id : ObjectId
    transaction_category_id : ObjectId
    created_at : datetime
    updated_at : datetime

    class Config:
        collection ="merchant_product_transaction_categories"
#         arbitrary_types_allowed = True


class giftcard_denominations(Model):
    version : ObjectId
    denomination_value : float
    active : bool
    modified_by : ObjectId
    created_at : datetime
    updated_at :datetime

    class Config:
        collection = "giftcard_denominations"
#         arbitrary_types_allowed = True


class gifts(Model):
    version : ObjectId
    gift_status : str
    communication_method : str
    giftcard_id : ObjectId
    sender_id : ObjectId
    recipient_id : ObjectId
    user_order_detail_id : ObjectId
    provider_id : ObjectId
    provider_uid : str
    recipient_phone : str
    recipient_email : str
    recipient_first_name : str
    recipient_last_name : str
    sender_first_name : str
    sender_last_name : str
    access_pin : str
    message : str
    consecutive_failed_access_attempt_count : bool
    delivery_attempt_count : int
    scheduled_delivery_date : datetime
    sender_notified_flag : bool
    recipient_notified_flag : bool
    claim_token : str
    created_at :datetime
    updated_at :datetime
    delivered_at :datetime

    class Config:
        collection = "gifts"
#         arbitrary_types_allowed = True


class merchant_product_variants(Model):
    active : bool
    merchant_product_id : ObjectId
    variant_id : ObjectId
    created_at : datetime
    updated_at :datetime

    class Config:
        collection ="merchant_product_variants"
#         arbitrary_types_allowed = True


class user_order_details_giftcards(Model):
    version : ObjectId
    order_details_id : ObjectId
    giftcard_details_id : ObjectId
    modified_by : ObjectId
    created_at : datetime
    updated_at : datetime

    class Config:
        collection ="user_order_details_giftcards"
#         arbitrary_types_allowed = True
    

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
    

class user_addresses(Model):
    version : ObjectId
    active : bool
    user_id : ObjectId
    normalized_address_id : ObjectId
    address_street1 : str
    address_street2 : str
    address_city : str
    address_state : str
    address_country : str
    zip_code: str
    phone_number : str
    preferred_flag : bool
    notified_flag : bool
    validated_flag : bool
    created_at : datetime
    updated_at : datetime
    first_name : str
    last_name : str
    email : str
    mobile_number : str
    company_name : str

    class Config:
        collection ="user_addresses"
#         arbitrary_types_allowed = True


# class user_credit_cards(Model):
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


class countries(Model):
    country_name : str
    country_code : str
    region : str
    subregion: str
    created_at :datetime
    updated_at : datetime
    country_name_arabic : str
    
    class Config:
        collection = "countries"
#         arbitrary_types_allowed = True

class categories(Model):
    version : ObjectId
    category_name : str
    active : bool
    sort_order : float
    modified_by : ObjectId
    created_at :datetime
    updated_at :datetime
    category_type : str
    category_image : str
    banner : str
    banner_arabic : str
    category_name_arabic :str

    class Config:
        collection ="categories"
#         arbitrary_types_allowed = True
        


class redemption_partners(Model):
    version : ObjectId
    active : bool
    partner_name : str
    partner_name_arabic : str
    country_id : ObjectId
    partner_logo: str
    created_at :datetime
    updated_at : datetime

    class Config:
        collection = "redemption_partners"
#         arbitrary_types_allowed = True


class user_openids(Model):
    version : ObjectId
    user_id : ObjectId
    provider_id : ObjectId
    provider_uid : str
    identifier_url : str
    name : str
    email : str
    verified_email: str
    avatar_url : str
    access_token : str
    expires_at :datetime
    gender : str
    birthday : datetime
    default_openid_flag : bool
    notified_flag : bool
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "user_openids"
#         arbitrary_types_allowed = True



class user_phone_logins(Model):
    version : ObjectId
    active : bool
    user_id : ObjectId
    normalized_phone : str
    reset_password_token : str
    reset_password_sent_at : datetime
    reset_password_token_expires_at : datetime
    password_reset_at : datetime
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "user_phone_logins"
#        arbitrary_types_allowed = True


class transaction_categories(Model):
    version : ObjectId
    category_name : str
    active : bool
    private_category_flag : bool
    user_id : ObjectId
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "transaction_categories"
#         arbitrary_types_allowed = True



class giftcard_variety_denominations(Model):
    version : ObjectId
    active : bool
    giftcard_variety_id : ObjectId
    giftcard_denomination_id : ObjectId
    modified_by : ObjectId
    created_at : datetime
    updated_at :datetime

    class Config:
        collection = "giftcard_variety_denominations"
#         arbitrary_types_allowed = True

class giftcard_details(Model):
    version : ObjectId
    giftcard_id : ObjectId
    giftcard_variety_id : ObjectId
    delivery_method_id : ObjectId
    distributor_id : ObjectId
    multipack_quantity : bool
    issued_date : datetime
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "giftcard_details"
#         arbitrary_types_allowed = True


class third_party_order_details(Model):
    delivery_method_id : ObjectId
    third_party_order_id : ObjectId
    giftcard_variety_id : ObjectId
    card_number : str
    expiration_date :datetime
    original_value :float
    remaining_value : float
    card_pin : str
    order_detail_status : str
    created_at : datetime
    updated_at : datetime
    giftcard_detail_id : ObjectId
    giftcard_margin_rate: float
    card_url : str
    card_access_key : str

    class Config:
        collection = "third_party_order_details"
#         arbitrary_types_allowed = True



class user_orders(Model):
    version : ObjectId
    order_status : str
    user_id : ObjectId
    payment_method_id : ObjectId
    shipping_address_id : ObjectId
    distributor_transaction_id : ObjectId
    reward_program_transaction_id : ObjectId
    order_total : float
    orderid : str
    payment_refno : str
    payment_message : str
    created_at : datetime
    updated_at : datetime
    total_amount : float
    order_type : str
    user_distributor_transaction_id : ObjectId
    payment_fee : float
    current_exchange_rate :float
    language_code : str
    order_message : str
    payment_session_id : str
    amount_paid_in_sar : float
    points_exchange_member_id : str
    points : ObjectId
    converted_points : ObjectId

    class Config:
        collection = "user_orders"
#         arbitrary_types_allowed = True




class offer_order_details(Model):
    version : ObjectId
    order_details_status: str
    offer_order_id : ObjectId
    offer_campaign_id : ObjectId
    offer_value : float
    quantity : ObjectId
    created_at :datetime
    updated_at : datetime
    store_name : str
    gift_message : str
    recipient_email : str
    recipient_phone : str

    class Config:
        collection = "offer_order_details"
#         arbitrary_types_allowed = True



class giftcard_batch_giftcard_details(Model):
    version : ObjectId
    giftcard_batch_id : ObjectId
    giftcard_details_id : ObjectId
    supplier_rate : int
    created_at : datetime
    updated_at : datetime 

    class Config:
        collection = "giftcard_batch_giftcard_details"
#         arbitrary_types_allowed = True


class giftcard_style_images(Model):
    giftcard_style_id : ObjectId
    image : str
    default_image_flag : bool
    image_processing : bool
    created_at :datetime
    updated_at : datetime
    banner : str
    logo : str

    class Config:
        collection = "giftcard_style_images"
#         arbitrary_types_allowed = True



class merchant_product_terms(Model):
    merchant_product_id : ObjectId
    terms_text : str
    language : str
    created_at :datetime
    updated_at : datetime

    class Config:
        collection = "merchant_product_terms"
#         arbitrary_types_allowed = True


class merchant_products(Model):
    active : bool
    brand_id : ObjectId
    giftcard_unit_id : ObjectId
    product_name : str
    product_name_arabic : str
    weight : str
    sku : str
    retail_price : float
    shipping_cost : float
    sales_tax :float
    vat :float
    total_cost : float
    warranty : int
    expiration_date : datetime
    description : str
    description_arabic :str
    created_at : datetime
    updated_at : datetime
    expected_delivery_days : ObjectId
    product_id : str

    class Config:
        collection = "merchant_products"
#         arbitrary_types_allowed = True
    

class variant_values(Model):
    active : bool
    variant_id : ObjectId
    value_name : str
    value_code : str
    created_at : datetime
    updated_at : datetime
    value_name_arabic: str
    color_code : str

    class Config:
        collection = "variant_values"
#         arbitrary_types_allowed = True


class offer_orders(Model):
    order_status: str
    user_id : ObjectId
    order_total : float
    orderid : str
    payment_refno : str
    payment_message : str
    payment_fee : float
    current_exchange_rate : float
    language_code : str
    order_message : str
    payment_session_id : str
    amount_paid_in_sar :float
    points : ObjectId
    created_at :datetime
    updated_at :datetime
    price_in_points : ObjectId
    payment_method_id : ObjectId
    is_gift : bool
    batch_id : str
    offer_url : str

    class Config:
        collection = "offer_orders"
#         arbitrary_types_allowed = True


# class role_entitlements(Model):
#     version : ObjectId
#     role_id : ObjectId
#     entitlement_id : ObjectId
#     required_flag : bool
#     default_flag : bool
#     created_at :datetime
#     updated_at :datetime

#     class Config:
#         collection = "role_entitlements"
#         arbitrary_types_allowed = True


class giftcard_varieties(Model):
    version : ObjectId
    active : bool
    giftcard_type_id : ObjectId
    giftcard_tags_id : ObjectId
    activation_required_flag : bool
    no_expiration_flag : bool
    validation_required_flag : bool
    barcode_required_flag : bool
    one_time_use_flag : bool
    flex_init_amount_flag : bool
    amount :  Optional[int]
    max_init_amount :float
    min_init_amount : float
    variety_description : str
    reloadable_flag : Optional[bool]
    giftcard_denomination_flag : Optional[bool]
    balance_check_url : str
    modified_by : ObjectId
    created_at :datetime
    updated_at :datetime
    online_flag : bool
    offline_flag : bool
    online_redemption_instructions :str
    offline_redemption_instructions : str
    remote_giftcard_url : str
    short_description :str
    variety_source : str
    custom_variety_flag : bool
    giftcard_variety_reference_no : str
    distributor_id : ObjectId
    multilingual_flag : bool
    short_description_arabic : str

    class Config:
        collection = "giftcard_varieties"
#         arbitrary_types_allowed = True


class schema_migrations(Model):
    version : str

    class Config:
        collection = "schema_migrations"
#         arbitrary_types_allowed = True


class administrator_activity_logs(Model):
    version : ObjectId
    administrator_id : ObjectId
    ip_address : str
    activity_name : str
    activity_starts_at :datetime
    activity_ends_at :datetime
    status : str
    description: str
    entity_name : str
    entity_value : str
    created_at :datetime
    updated_at :datetime

    class Config:
        collection = "schema_migrations"
#         arbitrary_types_allowed = True


class normalized_addresses(Model):
    version : ObjectId
    avs_address1 : str
    avs_address2 : str
    avs_phone_number : str
    created_at : datetime
    updated_at :datetime

    class Config:
        collection = "normalized_addresses"
#         arbitrary_types_allowed = True


class user_emails(Model):
    version : ObjectId
    user_id : ObjectId
    email : str
    normalized_email : str
    default_email_flag : bool
    verified_email_flag : bool
    notified_flag : bool
    confirmation_token : str
    confirmed_at : datetime
    confirmation_sent_at :datetime
    confirmation_expires_at :datetime
    created_at : datetime
    updated_at :datetime

    class Config:
        collection = "user_emails"
#         arbitrary_types_allowed = True


class offer_campaign_transaction_categories(Model):
    active : bool
    offer_campaign_id : ObjectId
    transaction_category_id : ObjectId
    created_at : datetime
    updated_at : datetime

    class Config:
        collection = "offer_campaign_transaction_categories"
#         arbitrary_types_allowed = True

