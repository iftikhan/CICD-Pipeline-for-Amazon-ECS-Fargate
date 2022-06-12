from typing import Collection, List, Optional
from bson.json_util import dumps,loads,default
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine, Model, ObjectId
from odmantic.bson import ObjectId
from pydantic import BaseModel
import json
from app.login.auth import AuthHandler
from app.models.models import (Merchant_product_details, brand_categories,
                               brand_category_transaction_categories,
                               brand_images, brands, categories, countries,
                               delivery_methods, experience_details,
                               experience_images, experience_order_details,
                               experience_order_recipients, experience_orders,
                               experience_prices, experience_slots,
                               giftcard_attribute_values, giftcard_attributes,
                               giftcard_batch_giftcard_details,
                               giftcard_batches, giftcard_denominations,
                               giftcard_details, giftcard_style_images,
                               giftcard_styles, giftcard_terms, giftcard_types,
                               giftcard_units, giftcard_varieties,
                               giftcard_variety_brands,
                               giftcard_variety_denominations, giftcards,
                               gifts, homepage_banners, interface_methods,
                               merchant_product_categories,
                               merchant_product_detail_variant_values,
                               merchant_product_images,
                               merchant_product_order_details,
                               merchant_product_orders, merchant_product_terms,
                               merchant_product_transaction_categories,
                               merchant_product_variants, merchant_products,
                               normalized_addresses, offer_campaign_categories,
                               offer_campaign_images, offer_campaign_terms,
                               offer_campaign_transaction_categories,
                               offer_campaigns, offer_order_details,
                               offer_orders, openid_providers,
                               Partner_category_details, point_transactions,
                               redemption_partners, schema_migrations,
                               supplier_access_logs, #supplier_accounts,
                               suppliers, third_party_brands,
                               third_party_order_details,
                               transaction_categories, user_addresses,
                               user_emails, user_openids, user_order_details,
                               user_order_details_giftcards, user_orders,
                               user_phones,variant_values, variants,
                               wallet_giftcards, wallets, whitelisted_proxies,
                               organization,
                               gift_card_length
                               ,language,redemption_method,activation_required,product_category,weight,shipping_cost,warranty,
                               sales,mapping_for,select_colors,vat,partner,giftcard_prefix,tags,description,documentation)
from app.models.models_update import (
    Merchant_product_details_update, brand_categories_update,
    brand_category_transaction_categories_update, brand_images_update,
    brands_update, categories_update, countries_update,
    delivery_methods_update, experience_details_update,
    experience_images_update, experience_order_details_update,
    experience_order_recipients_update, experience_orders_update,
    experience_slots_update, giftcard_attribute_values_update,
    giftcard_attributes_update, giftcard_batch_giftcard_details_update,
    giftcard_batches_update, giftcard_denominations_update,
    giftcard_details_update, giftcard_style_images_update,
    giftcard_styles_update, giftcard_terms_update, giftcard_types_update,
    giftcard_units_update, giftcard_varieties_update,
    giftcard_variety_brands_update, giftcard_variety_denominations_update,
    giftcards_update, gifts_update, homepage_banners_update,
    interface_methods_update, merchant_product_categories_update,
    merchant_product_detail_variant_values_update,
    merchant_product_images_update, merchant_product_order_details_update,
    merchant_product_orders_update, merchant_product_terms_update,
    merchant_product_transaction_categories_update,
    merchant_product_variants_update, merchant_products_update,
    normalized_addresses_update, offer_campaign_categories_update,
    offer_campaign_images_update, offer_campaign_terms_update,
    offer_campaign_transaction_categories_update, offer_campaigns_update,
    offer_order_details_update, offer_orders_update, openid_providers_update,
    Partner_category_details_update,point_transactions_update, redemption_partners_update,
    schema_migrations_update, supplier_access_logs_update,
    #supplier_accounts_update, 
    suppliers_update, third_party_brands_update,
    third_party_order_details_update, transaction_categories_update,
    user_addresses_update, user_emails_update, user_openids_update,
    user_order_details_giftcards_update, user_order_details_update,
    user_orders_update, user_phones_update,
    variant_values_update, variants_update, wallet_giftcards_update,
    wallets_update, whitelisted_proxies_update
    ,organization_update,gift_card_length_update
    ,language_update,redemption_method_update,activation_required_update,
    product_category_update,weight_update,shipping_cost_update,warranty_update,sales_update,
    mapping_for_update,select_colors_update,vat_update,partner_update,giftcard_prefix_update,
    tags_update,description_update,documentation_update)

app = FastAPI(title="Loyalty & GiftCard API's",
    description="API details for Loyalty and GiftCards",
    version="0.0.1",
    terms_of_service="http://repletech.com/terms/",
    contact={
        "name": "Repletech",
        "url": "http://repletech.com/contact/",
        "email": "info@repletech.com",
    },
    license_info={
        "name": "Repletech License",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    )
app.add_middleware(CORSMiddleware,    allow_origins=["*"],    allow_methods=["*"],    allow_headers=["*"],    allow_credentials=True )
auth_handler = AuthHandler()
class Tree(Model):
    name: str
    average_size: float
    discovery_year: int
class TreePatchSchema(BaseModel):
    name: Optional[str]
    average_size: Optional[float]
    discovery_year: Optional[float]

client = AsyncIOMotorClient("mongodb://admin:admin@mongoserver:27017/")
#client = AsyncIOMotorClient("mongodb://admin:admin@localhost:27017/")
engine = AIOEngine(motor_client=client, database="ehadaya")
print(client.list_databases)

@app.put("/trees/", response_model=Tree)
async def create_tree(tree: Tree):
    await engine.save(tree)
    return tree


@app.get("/trees/", response_model=List[Tree])
async def get_trees():
    trees = await engine.find(Tree)
    return trees

@app.get("/trees/count", response_model=int)
async def count_trees():
    count = await engine.count(Tree)
    return count

@app.get("/trees/{id}", response_model=Tree)
async def get_tree_by_id(id: ObjectId):
    tree = await engine.find_one(Tree, Tree.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree
@app.patch("/trees/{id}", response_model=Tree)
async def update_tree_by_id(id: ObjectId, patch: TreePatchSchema):
    tree = await engine.find_one(Tree, Tree.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree
######
@app.get("/fetchcountry/",tags = ["Fetch Country"])
def fetch_all_countries():
    from pymongo import MongoClient
    #MONGOSRV_URL = 'mongodb://admin:admin@15.185.134.17:27017/'
    MONGOSRV_URL = 'mongodb://admin:admin@mongoserver:27017/'
    mclient = MongoClient(MONGOSRV_URL)
    filter={}
    project={
        'iso2': 1,
        'name':1,
        'iso3':1
    }
    result = mclient['ehadaya']['countries'].find(
    filter=filter,
    projection=project
    )
    json_data = json.dumps(list(result),default=default)
    json_loads =json.loads(json_data)
    if json_loads :
        return json_loads
    else:
        return {}

@app.get("/fetchcountry/{countrycode}",tags = ["Fetch Country"])
def fetch_countries(countrycode : str):
    from pymongo import MongoClient
    #MONGOSRV_URL = 'mongodb://admin:admin@15.185.134.17:27017/'
    MONGOSRV_URL = 'mongodb://admin:admin@mongoserver:27017/'
    mclient = MongoClient(MONGOSRV_URL)
    filter={
        'iso2': countrycode
    }
    project={
        'iso2': 1, 
        'name':1,
        'currency': 1,
        'currency_symbol': 1, 
        'region': 1, 
        'subregion': 1, 
        'latitude': 1, 
        'longitude': 1, 
        'phone_code': 1, 
        'emoji': 1, 
        '_id': 1,  
        'states.latitude': 1, 
        'states.longitude': 1, 
        'states.id': 1, 
        'states.name': 1, 
        'states.code': 1, 
        'states.cities.id': 1, 
        'states.cities.name': 1, 
        'states.cities.latitude': 1, 
        'states.cities.longitude': 1
    }
    
    result = mclient['ehadaya']['countries'].find(
        filter=filter,
        projection=project
    )
    #df =  pd.DataFrame(list(cursor))
    json_data = json.dumps(list(result),default=default)
    json_loads =json.loads(json_data)
    if json_loads :
        return json_loads
    else:
        return {}
######
@app.put("/language/", response_model=language,tags = ["language"])
async def create_language(tree: language,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/language/", response_model=List[language],tags = ["language"])
async def get_language(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(language)
    return trees

@app.get("/language/{id}", response_model=language,tags = ["language"])
async def get_language_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(language, language.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/language/{id}", response_model=language,tags = ["language"])
async def get_language_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(language, language.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/language/{id}", response_model=language,tags = ["language"])
async def update_language_id(id: ObjectId, patch: language_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(language, language.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/language/{id}", response_model=language,tags = ["language"])
async def delete_language_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(language, language.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
######
@app.put("/redemption_method/", response_model=redemption_method,tags = ["redemption_method"])
async def create_redemption_method(tree: redemption_method,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/redemption_method/", response_model=List[redemption_method],tags = ["redemption_method"])
async def get_redemption_method(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(redemption_method)
    return trees

@app.get("/redemption_method/{id}", response_model=redemption_method,tags = ["redemption_method"])
async def get_redemption_method_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(redemption_method, redemption_method.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/redemption_method/{id}", response_model=redemption_method,tags = ["redemption_method"])
async def get_redemption_method_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(language, language.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/redemption_method/{id}", response_model=redemption_method,tags = ["redemption_method"])
async def update_redemption_method_id(id: ObjectId, patch: redemption_method_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(redemption_method, redemption_method.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/redemption_method/{id}", response_model=redemption_method,tags = ["redemption_method"])
async def delete_redemption_method_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = engine.find_one(redemption_method, redemption_method.id == id)
    if tree is None:
        raise HTTPException(404)
    engine.delete(tree)
    return tree
######

@app.put("/activation_required/", response_model=activation_required,tags = ["activation_required"])
async def create_activation_required(tree: activation_required,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/activation_required/", response_model=activation_required,tags = ["activation_required"])
async def get_activation_required(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(activation_required)
    return trees

@app.get("/activation_required/", response_model=List[activation_required],tags = ["activation_required"])
async def get_activation_required(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(activation_required)
    return trees

@app.get("/activation_required/{id}", response_model=activation_required,tags = ["activation_required"])
async def get_activation_required_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(activation_required, activation_required.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/activation_required/{id}", response_model=activation_required,tags = ["activation_required"])
async def update_activation_required_id(id: ObjectId, patch: activation_required_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(activation_required, activation_required.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/activation_required/{id}", response_model=activation_required,tags = ["activation_required"])
async def delete_activation_required_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(activation_required, activation_required.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
#######

@app.put("/tags/", response_model=tags,tags = ["tags"])
async def create_tags(tree: tags,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/tags/", response_model=tags,tags = ["tags"])
async def get_tags(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(tags)
    return trees

@app.get("/tags/", response_model=List[tags],tags = ["tags"])
async def get_tags(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(tags)
    return trees

@app.get("/tags/{id}", response_model=tags,tags = ["tags"])
async def get_tags_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(tags, tags.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/tags/{id}", response_model=tags,tags = ["tags"])
async def update_tags_id(id: ObjectId, patch: tags_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(tags, tags.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/tags/{id}", response_model=tags,tags = ["tags"])
async def delete_tags_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(tags, tags.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
#######

@app.put("/description/", response_model=description,tags = ["description"])
async def create_description(tree: description,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/description/", response_model=description,tags = ["description"])
async def get_description(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(description)
    return trees

@app.get("/description/", response_model=List[description],tags = ["description"])
async def get_description(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(description)
    return trees

@app.get("/description/{id}", response_model=description,tags = ["description"])
async def get_description_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(description, description.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/description/{id}", response_model=description,tags = ["description"])
async def update_description_id(id: ObjectId, patch: description_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(description, description.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/description/{id}", response_model=description,tags = ["description"])
async def delete_description_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(description, description.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
#######


@app.put("/documentation/", response_model=documentation,tags = ["documentation"])
async def create_documentation(tree: documentation,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/documentation/", response_model=documentation,tags = ["documentation"])
async def get_documentation(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(documentation)
    return trees

@app.get("/documentation/", response_model=List[documentation],tags = ["documentation"])
async def get_documentation(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(documentation)
    return trees

@app.get("/documentation/{id}", response_model=documentation,tags = ["documentation"])
async def get_documentation_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(documentation, documentation.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/documentation/{id}", response_model=documentation,tags = ["documentation"])
async def update_documentation_id(id: ObjectId, patch: documentation_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(documentation, documentation.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/documentation/{id}", response_model=documentation,tags = ["documentation"])
async def delete_documentation_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(documentation, documentation.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
#######
@app.put("/warranty/", response_model=warranty,tags = ["warranty"])
async def create_warranty(tree: warranty,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/warranty/", response_model=List[warranty],tags = ["warranty"])
async def get_warranty(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(warranty)
    return trees

@app.post("/warranty/", response_model=warranty,tags = ["warranty"])
async def get_warranty(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(warranty)
    return trees

@app.get("/warranty/{id}", response_model=warranty,tags = ["warranty"])
async def get_warranty_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(warranty, warranty.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/warranty/{id}", response_model=warranty,tags = ["warranty"])
async def get_warranty_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(warranty, warranty.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/warranty/{id}", response_model=warranty,tags = ["warranty"])
async def update_warranty_id(id: ObjectId, patch: warranty_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(warranty, warranty.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/warranty/{id}", response_model=warranty,tags = ["warranty"])
async def delete_warranty_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(warranty, warranty.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

######
@app.put("/product_category/", response_model=product_category,tags = ["product_category"])
async def create_product_category(tree: product_category,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/product_category/", response_model=List[product_category],tags = ["product_category"])
async def get_product_category(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(product_category)
    return trees

@app.post("/product_category/", response_model=product_category,tags = ["product_category"])
async def get_product_category(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(product_category)
    return trees

@app.get("/product_category/{id}", response_model=product_category,tags = ["product_category"])
async def get_product_category_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(product_category, product_category.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/product_category/{id}", response_model=product_category,tags = ["product_category"])
async def get_product_category_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(product_category, product_category.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/product_category/{id}", response_model=product_category,tags = ["product_category"])
async def update_product_category_id(id: ObjectId, patch: product_category_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(product_category, product_category.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/product_category/{id}", response_model=product_category,tags = ["product_category"])
async def delete_product_category_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(product_category, product_category.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

#####


@app.put("/weight/", response_model=weight,tags = ["weight"])
async def create_weight(tree: weight,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/weight/", response_model=List[weight],tags = ["weight"])
async def get_weight(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(weight)
    return trees

@app.post("/weight/", response_model=weight,tags = ["weight"])
async def get_weight(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(weight)
    return trees

@app.get("/weight/{id}", response_model=weight,tags = ["weight"])
async def get_weight_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(weight, weight.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/weight/{id}", response_model=weight,tags = ["weight"])
async def get_weight_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(weight, weight.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/weight/{id}", response_model=weight,tags = ["weight"])
async def update_weight_id(id: ObjectId, patch: weight_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(weight, weight.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/weight/{id}", response_model=weight,tags = ["weight"])
async def delete_weight_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(weight, weight.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
######

@app.put("/shipping_cost/", response_model=shipping_cost,tags = ["shipping_cost"])
async def create_shipping_cost(tree: shipping_cost,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/shipping_cost/", response_model=List[shipping_cost],tags = ["shipping_cost"])
async def get_shipping_cost(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(shipping_cost)
    return trees

@app.post("/shipping_cost/", response_model=shipping_cost,tags = ["shipping_cost"])
async def get_shipping_cost(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(shipping_cost)
    return trees

@app.get("/shipping_cost/{id}", response_model=shipping_cost,tags = ["shipping_cost"])
async def get_shipping_cost_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(shipping_cost, shipping_cost.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

# @app.get("/shipping_cost/{id}", response_model=shipping_cost,tags = ["shipping_cost"])
# async def get_shipping_cost_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     tree = await engine.find_one(shipping_cost, shipping_cost.id == id)
#     if tree is None:
#         raise HTTPException(404)
#     return tree

@app.patch("/shipping_cost/{id}", response_model=shipping_cost,tags = ["shipping_cost"])
async def update_shipping_cost_id(id: ObjectId, patch: shipping_cost_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(shipping_cost, shipping_cost.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/shipping_cost/{id}", response_model=shipping_cost,tags = ["shipping_cost"])
async def delete_shipping_cost_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(shipping_cost, shipping_cost.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

######
@app.put("/sales/", response_model=sales,tags = ["sales"])
async def create_sales(tree: sales,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/sales/", response_model=List[sales],tags = ["sales"])
async def get_sales(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(sales)
    return trees

@app.post("/sales/", response_model=sales,tags = ["sales"])
async def get_sales(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(sales)
    return trees

@app.get("/sales/{id}", response_model=sales,tags = ["sales"])
async def get_sales_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(sales, sales.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/sales/{id}", response_model=sales,tags = ["sales"])
async def get_sales_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(sales, sales.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/sales/{id}", response_model=sales,tags = ["sales"])
async def update_sales_id(id: ObjectId, patch: sales_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(sales, sales.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/sales/{id}", response_model=sales,tags = ["sales"])
async def delete_sales_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(sales, sales.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

######
@app.put("/mapping_for/", response_model=mapping_for,tags = ["mapping_for"])
async def create_mapping_for(tree: mapping_for,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/mapping_for/", response_model=List[mapping_for],tags = ["mapping_for"])
async def get_mapping_for(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(mapping_for)
    return trees

@app.post("/mapping_for/", response_model=mapping_for,tags = ["mapping_for"])
async def get_mapping_for(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(mapping_for)
    return trees

@app.get("/mapping_for/{id}", response_model=mapping_for,tags = ["mapping_for"])
async def get_mapping_for_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(mapping_for, mapping_for.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/mapping_for/{id}", response_model=mapping_for,tags = ["mapping_for"])
async def get_mapping_for_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(mapping_for, mapping_for.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/mapping_for/{id}", response_model=mapping_for,tags = ["mapping_for"])
async def update_mapping_for_id(id: ObjectId, patch: mapping_for_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(mapping_for, mapping_for.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/mapping_for/{id}", response_model=mapping_for,tags = ["mapping_for"])
async def delete_mapping_for_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(mapping_for, mapping_for.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

######

@app.put("/select_colors/", response_model=select_colors,tags = ["select_colors"])
async def create_select_colors(tree: select_colors,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/select_colors/", response_model=List[select_colors],tags = ["select_colors"])
async def get_select_colors(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(select_colors)
    return trees

@app.post("/select_colors/", response_model=select_colors,tags = ["select_colors"])
async def get_select_colors(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(select_colors)
    return trees

@app.get("/select_colors/{id}", response_model=select_colors,tags = ["select_colors"])
async def get_select_colors_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(select_colors, select_colors.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/select_colors/{id}", response_model=select_colors,tags = ["select_colors"])
async def get_select_colors_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(select_colors, select_colors.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/select_colors/{id}", response_model=select_colors,tags = ["select_colors"])
async def update_select_colors_id(id: ObjectId, patch: select_colors_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(select_colors, select_colors.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/select_colors/{id}", response_model=select_colors,tags = ["select_colors"])
async def delete_select_colors_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(select_colors, select_colors.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
######

@app.put("/vat/", response_model=vat,tags = ["vat"])
async def create_vat(tree: vat,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/vat/", response_model=List[vat],tags = ["vat"])
async def get_vat(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(vat)
    return trees

@app.post("/vat/", response_model=vat,tags = ["vat"])
async def get_vat(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(vat)
    return trees

@app.get("/vat/{id}", response_model=vat,tags = ["vat"])
async def get_vat_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(vat, vat.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.get("/vat/{id}", response_model=vat,tags = ["vat"])
async def get_vat_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(vat, vat.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/vat/{id}", response_model=vat,tags = ["vat"])
async def update_vat_id(id: ObjectId, patch: vat_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(vat, vat.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/vat/{id}", response_model=vat,tags = ["vat"])
async def delete_vat_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(vat, vat.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

######
@app.put("/gift_card_length/", response_model=gift_card_length,tags = ["gift_card_length"])
async def create_gift_card_length(tree: gift_card_length,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/gift_card_length/", response_model=gift_card_length,tags = ["gift_card_length"])
async def post_gift_card_length(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(gift_card_length)
    return trees

@app.get("/gift_card_length/", response_model=List[gift_card_length],tags = ["gift_card_length"])
async def get_gift_card_length(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(gift_card_length)
    return trees

@app.get("/gift_card_length/{id}", response_model=gift_card_length,tags = ["gift_card_length"])
async def get_gift_card_length_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(gift_card_length, gift_card_length.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/gift_card_length/{id}", response_model=gift_card_length,tags = ["gift_card_length"])
async def update_gift_card_length_id(id: ObjectId, patch: gift_card_length_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(gift_card_length, gift_card_length.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
        print(tree)
    await engine.save(tree)
    return tree

@app.delete("/gift_card_length/{id}", response_model=gift_card_length,tags = ["gift_card_length"])
async def delete_gift_card_length_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(gift_card_length, gift_card_length.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

######
@app.put("/organization/", response_model=organization,tags = ["organization"])
async def create_organization(tree: organization,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/organization/", response_model=List[organization],tags = ["organization"])
async def get_organization(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(organization)
    return trees

@app.get("/organization/count", response_model=int,tags = ["organization"])
async def count_organization(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    count = await engine.count(organization)
    return count

@app.get("/organization/{id}", response_model=organization,tags = ["organization"])
async def get_tree_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(organization, organization.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/organization/{id}", response_model=organization,tags = ["organization"])
async def update_tree_by_id(id: ObjectId, patch: organization_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(organization, organization.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    print(f"after {tree}")
    return tree

@app.delete("/organization/{id}", response_model=organization,tags = ["organization"])
async def delete_organization_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(organization, organization.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

#######

@app.put("/giftcard_prefix/", response_model=giftcard_prefix,tags = ["giftcard_prefix"])
async def create_giftcard_prefix(tree: giftcard_prefix,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_prefix", response_model=giftcard_prefix, tags = ["giftcard_prefix"])
async def get_giftcard_prefix(tree: giftcard_prefix,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_prefix/", response_model=List[giftcard_prefix],tags = ["giftcard_prefix"])
async def get_giftcard_prefix(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_prefix)
    return trees

@app.get("/giftcard_prefix/{id}", response_model=giftcard_prefix,tags = ["giftcard_prefix"])
async def get_tree_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_prefix, giftcard_prefix.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/giftcard_prefix/{id}", response_model=giftcard_prefix,tags = ["giftcard_prefix"])
async def update_tree_by_id(id: ObjectId, patch: giftcard_prefix_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_prefix, giftcard_prefix.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    print(f"after {tree}")
    return tree

@app.delete("/giftcard_prefix/{id}", response_model=giftcard_prefix,tags = ["giftcard_prefix"])
async def delete_gift_card_prefix_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_prefix, giftcard_prefix.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
#######
@app.put("/partner_category", response_model=Partner_category_details, tags = ["Partner_category_details"])
async def partner_category(tree: Partner_category_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/partner_category", response_model=Partner_category_details, tags = ["Partner_category_details"])
async def partner_category(tree: Partner_category_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/partner_category",response_model= List[Partner_category_details],tags = ["Partner_category_details"])
async def get_partner_category(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(Partner_category_details)
    return trees

@app.get("/partner_category/{id}", response_model=Partner_category_details,tags = ["Partner_category_details"])
async def get_tree_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree = await engine.find_one(Partner_category_details, Partner_category_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/partner_category/{id}", response_model=Partner_category_details,tags = ["Partner_category_details"])
async def update_partner_category_detail_by_id(id: ObjectId, patch: Partner_category_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(Partner_category_details, Partner_category_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/partner_category/{id}", response_model=Partner_category_details,tags = ["Partner_category_details"])
async def delete_merchant_product_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(Partner_category_details, Partner_category_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.get("/merchant_product_details",response_model= List[Merchant_product_details],tags = ["Merchant_product_details"])
async def get_merchant_product_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(Merchant_product_details)
    return trees

@app.put("/Merchant_product_details", response_model=Merchant_product_details, tags = ["Merchant_product_details"])
async def Merchant_product_detail(tree: Merchant_product_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/Merchant_product_details", response_model=Merchant_product_details, tags = ["Merchant_product_details"])
async def Merchant_product_detail(tree: Merchant_product_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/merchant_product_details/{id}", response_model=Merchant_product_details,tags = ["Merchant_product_details"])
async def get_tree_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree = await engine.find_one(Merchant_product_details, Merchant_product_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/merchant_product_detail/{id}", response_model=Merchant_product_details,tags = ["Merchant_product_details"])
async def update_merchant_product_detail_by_id(id: ObjectId, patch: Merchant_product_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(Merchant_product_details, Merchant_product_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/merchant_product_detail/{id}", response_model=Merchant_product_details,tags = ["Merchant_product_details"])
async def delete_merchant_product_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(Merchant_product_details, Merchant_product_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.put("/giftcard_attribute_values", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def giftcard_attribute_value(tree: giftcard_attribute_values,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_attribute_values", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def giftcard_attribute_value(tree: giftcard_attribute_values,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_attribute_values",response_model= List[giftcard_attribute_values],tags = ["giftcard_attribute_values"])
async def get_giftcard_attribute_values(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_attribute_values)
    return trees

@app.get("/giftcard_attribute_values/{id}", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def get_giftcard_attribute_values_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_attribute_values, giftcard_attribute_values.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/giftcard_attribute_values/{id}", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def update_giftcard_attribute_values_by_id(id: ObjectId, patch: giftcard_attribute_values_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_attribute_values, giftcard_attribute_values.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/giftcard_attribute_value/{id}", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def delete_giftcard_attribute_values_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_attribute_values, giftcard_attribute_values.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.put("/merchant_product_orders", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def merchant_product_order(tree: merchant_product_orders,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.put("/merchant_product_orders", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def merchant_product_order(tree: merchant_product_orders,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/merchant_product_orders",response_model= List[merchant_product_orders],tags = ["merchant_product_orders"])
async def get_merchant_product_orders(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees =await engine.find(merchant_product_orders)
    return trees

@app.get("/merchant_product_orders/{id}", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def get_merchant_product_orders_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree = await engine.find_one(merchant_product_orders, merchant_product_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/merchant_product_orders/{id}", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def update_merchant_product_orders_by_id(id: ObjectId, patch: merchant_product_orders_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(merchant_product_orders, merchant_product_orders.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/merchant_product_orders/{id}", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def delete_merchant_product_orders_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(merchant_product_orders, merchant_product_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

#####
@app.put("/brand_categories", response_model=brand_categories,tags = ["brand_categories"])
async def put_brand_categories(tree: brand_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/brand_categories", response_model=brand_categories,tags = ["brand_categories"])
async def post_brand_categories(tree: brand_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/brand_categories",response_model= List[brand_categories],tags = ["brand_categories"])
async def get_brand_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(brand_categories)
    return trees

@app.get("/brand_category_by/{id}", response_model=brand_categories,tags = ["brand_categories"])
async def get_brand_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree = engine.find_one(brand_categories, brand_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/brand_categories/{id}", response_model=brand_categories,tags = ["brand_categories"])
async def update_brand_categories_by_id(id: ObjectId, patch: brand_categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(brand_categories, brand_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/brand_categories/{id}", response_model=brand_categories,tags = ["brand_categories"])
async def delete_brand_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(brand_categories, brand_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree
#######
@app.put("/brand_category_transaction_categories", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def brand_category_transaction_categorie(tree: brand_category_transaction_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/brand_category_transaction_categories", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def brand_category_transaction_categorie(tree: brand_category_transaction_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/brand_category_transaction_categories",response_model= List[brand_category_transaction_categories],tags = ["brand_category_transaction_categories"])
async def get_brand_category_transaction_categoriess(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(brand_category_transaction_categories)
    return trees

@app.get("/brand_categories/{id}", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def get_brand_category_transaction_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree = await engine.find_one(brand_category_transaction_categories, brand_category_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/brand_category_transaction_categories/{id}", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def update_brand_category_transaction_categories_by_id(id: ObjectId, patch: brand_category_transaction_categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(brand_category_transaction_categories, brand_category_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/brand_category_transaction_categories/{id}", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def delete_brand_category_transaction_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(brand_category_transaction_categories, brand_category_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.put("/user_order_details", response_model=user_order_details,tags = ["user_order_details"])
async def user_order_detail(tree: user_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/user_order_details", response_model=user_order_details,tags = ["user_order_details"])
async def user_order_detail(tree: user_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/user_order_details",response_model= List[user_order_details],tags = ["user_order_details"])
async def get_user_order_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(user_order_details)
    return trees

@app.get("/user_order_details/{id}", response_model=user_order_details,tags = ["user_order_details"])
async def get_user_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(user_order_details, user_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.patch("/user_order_details/{id}", response_model=user_order_details,tags = ["user_order_details"])
async def update_user_order_details_by_id(id: ObjectId, patch: user_order_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(user_order_details, user_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.delete("/user_order_details/{id}", response_model=user_order_details,tags = ["user_order_details"])
async def delete_user_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(user_order_details, user_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.put("/merchant_product_detail_variant_values", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def merchant_product_detail_variant(tree: merchant_product_detail_variant_values,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/merchant_product_detail_variant_values", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def merchant_product_detail_variant(tree: merchant_product_detail_variant_values,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    engine.save(tree)
    return tree

@app.get("/merchant_product_detail_variant_values",response_model= List[merchant_product_detail_variant_values],tags = ["merchant_product_detail_variant_values"])
async def get_brand_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(merchant_product_detail_variant_values)
    return trees

@app.get("/merchant_product_detail_variant_values/{id}", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def get_merchant_product_detail_variant_values_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree = await engine.find_one(merchant_product_detail_variant_values, merchant_product_detail_variant_values.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_detail_variant_values/{id}", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def delete_merchant_product_detail_variant_values_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(merchant_product_detail_variant_values, merchant_product_detail_variant_values.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/merchant_product_detail_variant_values/{id}", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def update_merchant_product_detail_variant_values_by_id(id: ObjectId, patch: merchant_product_detail_variant_values_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(merchant_product_detail_variant_values, merchant_product_detail_variant_values.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/brand_images", response_model=brand_images,tags = ["brand_images"])
async def put_brand_images(tree: brand_images, file : UploadFile = Form(...),form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree['image'] = file
    await engine.save_all(tree,)
    return tree

@app.post("/brand_images", response_model=brand_images,tags = ["brand_images"])
async def post_brand_images(tree: brand_images, file : UploadFile = Form(...),form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree['image'] = file
    await engine.save_all(tree,)
    return tree

@app.get("/brand_images",response_model= List[brand_images],tags = ["brand_images"])
async def get_brand_images(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(brand_images)
    return trees

@app.get("/brand_images/{id}", response_model=brand_images,tags = ["brand_images"])
async def get_brand_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(brand_images, brand_images.id == id)
    if tree is None:
        raise HTTPException(404, detail= "ObjectID Not available")
    return tree

@app.delete("/brand_image/{id}", response_model=brand_images,tags = ["brand_images"])
async def delete_brand_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(brand_images, brand_images.id == id)
    if tree is None:
        raise HTTPException(status_code= 404, detail= "ObjectID Not available")
    await engine.delete(tree)
    return tree

@app.patch("/brand_images/{id}", response_model=brand_images,tags = ["brand_images"])
async def update_brand_images_by_id(id: ObjectId, patch: brand_images_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(brand_images, brand_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

# @app.patch("/update_brand_image/{id}", response_model=brand_images,tags = ["brand_images"])
# async def update_brand_image_by_id(id: ObjectId, image_name=  Form(...),  file : UploadFile = File(...)):    #patch: brand_image_update,
#     tree = await engine.find_one(brand_images, brand_images.id == id)
#     dic = {}
#     dic["image"] = file.filename
#     dic["name"] =  image_name
#     if tree is None:
#         raise HTTPException(404, detail= "ObjectID Not available")

#     patch_dict = dic   #exclude_unset=True
#     for name, value in patch_dict.items():
#         setattr(tree, name, value)
#     await engine.save(tree)
#     return tree

@app.put("/giftcard_batches", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def giftcard_batche(tree: giftcard_batches,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_batches", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def giftcard_batche(tree: giftcard_batches,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_batches",response_model= List[giftcard_batches],tags = ["giftcard_batches"])
async def get_giftcard_batches(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_batches)
    return trees

@app.get("/giftcard_batches/{id}", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def get_giftcard_batches_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_batches, giftcard_batches.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_batches/{id}", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def delete_giftcard_batches_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_batches, giftcard_batches.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_batches/{id}", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def update_giftcard_batches_by_id(id: ObjectId, patch: giftcard_batches_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_batches, giftcard_batches.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_variety_brands", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def giftcard_variety_brand(tree: giftcard_variety_brands,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_variety_brands", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def giftcard_variety_brand(tree: giftcard_variety_brands,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_variety_brands",response_model= List[giftcard_variety_brands],tags = ["giftcard_variety_brands"])
async def get_giftcard_variety_brands(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_variety_brands)
    return trees

@app.get("/giftcard_variety_brands/{id}", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def get_giftcard_variety_brands_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree = await engine.find_one(giftcard_variety_brands, giftcard_variety_brands.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_variety_brands/{id}", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def delete_giftcard_variety_brands_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_variety_brands, giftcard_variety_brands.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_variety_brands/{id}", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def update_giftcard_variety_brands_by_id(id: ObjectId, patch: giftcard_variety_brands_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(giftcard_variety_brands, giftcard_variety_brands.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/merchant_product_order_details", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def merchant_product_order_detail(tree: merchant_product_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/merchant_product_order_details", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def merchant_product_order_detail(tree: merchant_product_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/merchant_product_order_details",response_model= List[merchant_product_order_details],tags = ["merchant_product_order_details"])
async def get_merchant_product_order_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(merchant_product_order_details)
    return trees

@app.get("/merchant_product_order_details/{id}", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def get_merchant_product_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =await engine.find_one(merchant_product_order_details, merchant_product_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_order_details/{id}", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def delete_merchant_product_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(merchant_product_order_details, merchant_product_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/merchant_product_order_details/{id}", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def update_merchant_product_order_details_by_id(id: ObjectId, patch: merchant_product_order_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(merchant_product_order_details, merchant_product_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/experience_order_details", response_model=experience_order_details,tags = ["experience_order_details"])
async def experience_order_detail(tree: experience_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/experience_order_details", response_model=experience_order_details,tags = ["experience_order_details"])
async def experience_order_detail(tree: experience_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/experience_order_details",response_model= List[experience_order_details],tags = ["experience_order_details"])
async def get_experience_order_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(experience_order_details)
    return trees

@app.get("/experience_order_details/{id}", response_model=experience_order_details,tags = ["experience_order_details"])
async def get_experience_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(experience_order_details, experience_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_order_details/{id}", response_model=experience_order_details,tags = ["experience_order_details"])
async def delete_experience_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(experience_order_details, experience_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/experience_order_details/{id}", response_model=experience_order_details,tags = ["experience_order_details"])
async def update_experience_order_details_by_id(id: ObjectId, patch: experience_order_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(experience_order_details, experience_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/homepage_banners", response_model=homepage_banners,tags = ["homepage_banners"])
async def homepage_banner(tree: homepage_banners,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/homepage_banners", response_model=homepage_banners,tags = ["homepage_banners"])
async def homepage_banner(tree: homepage_banners,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/homepage_banners",response_model= List[homepage_banners],tags = ["homepage_banners"])
async def get_homepage_banners(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees =  await engine.find(homepage_banners)
    return trees

@app.get("/homepage_banners/{id}", response_model=homepage_banners,tags = ["homepage_banners"])
async def get_homepage_banners_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(homepage_banners, homepage_banners.id == id)
    if tree is None:
        raise HTTPException(status_code= 404)
    return tree

@app.delete("/homepage_banners/{id}", response_model=homepage_banners,tags = ["homepage_banners"])
async def delete_homepage_banners_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(homepage_banners, homepage_banners.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/homepage_banners/{id}", response_model=homepage_banners,tags = ["homepage_banners"])
async def update_homepage_banners_by_id(id: ObjectId, patch: homepage_banners_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(homepage_banners, homepage_banners.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/point_transactions", response_model=point_transactions,tags = ["point_transactions"])
async def point_transaction(tree: point_transactions,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/point_transactions", response_model=point_transactions,tags = ["point_transactions"])
async def point_transaction(tree: point_transactions,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/point_transactions",response_model= List[point_transactions],tags = ["point_transactions"])
async def get_point_transactions(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(point_transactions)
    return trees

@app.get("/point_transactions/{id}", response_model=point_transactions,tags = ["point_transactions"])
async def get_point_transactions_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(point_transactions, point_transactions.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/point_transactions/{id}", response_model=point_transactions,tags = ["point_transactions"])
async def delete_point_transactions_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(point_transactions, point_transactions.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/point_transactions/{id}", response_model=point_transactions,tags = ["point_transactions"])
async def update_point_transactions_by_id(id: ObjectId, patch: point_transactions_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(point_transactions, point_transactions.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/offer_campaign_images", response_model=offer_campaign_images,tags = ["offer_campaign_images"])
async def offer_campaign_image(tree: offer_campaign_images,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/offer_campaign_images",response_model= List[offer_campaign_images],tags = ["offer_campaign_images"])
async def get_offer_campaign_images(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(offer_campaign_images)
    return trees

@app.get("/offer_campaign_images/{id}", response_model=offer_campaign_images,tags = ["offer_campaign_images"])
async def get_offer_campaign_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(offer_campaign_images, offer_campaign_images.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_images/{id}", response_model=offer_campaign_images,tags = ["offer_campaign_images"])
async def delete_offer_campaign_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_images, offer_campaign_images.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/offer_campaign_images/{id}", response_model=offer_campaign_images ,tags = ["offer_campaign_images"])
async def update_offer_campaign_images_by_id(id: ObjectId, patch: offer_campaign_images_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_images, offer_campaign_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

# @app.post("/user_payment_methods", response_model=user_payment_methods)
# async def user_payment_method(tree: user_payment_methods):
#     await engine.save(tree)
#     return tree

@app.put("/giftcard_units", response_model=giftcard_units,tags = ["giftcard_units"])
async def giftcard_unit(tree: giftcard_units,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_units", response_model=giftcard_units,tags = ["giftcard_units"])
async def giftcard_unit(tree: giftcard_units,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_units",response_model= List[giftcard_units],tags = ["giftcard_units"])
async def get_giftcard_units(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_units)
    return trees

@app.get("/giftcard_units/{id}", response_model=giftcard_units,tags = ["giftcard_units"])
async def get_giftcard_units_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_units, giftcard_units.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_units/{id}", response_model=giftcard_units,tags = ["giftcard_units"])
async def delete_giftcard_units_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_units, giftcard_units.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_units/{id}", response_model=giftcard_units,tags = ["giftcard_units"])
async def update_giftcard_units_by_id(id: ObjectId, patch: giftcard_units_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_units, giftcard_units.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree
   
@app.put("/merchant_product_categories", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def merchant_product_categorie(tree: merchant_product_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/merchant_product_categories", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def merchant_product_categorie(tree: merchant_product_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/merchant_product_categories",response_model= List[merchant_product_categories],tags = ["merchant_product_categories"])
async def get_merchant_product_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(merchant_product_categories)
    return trees

@app.get("/merchant_product_categories/{id}", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def get_merchant_product_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(merchant_product_categories, merchant_product_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_categories/{id}", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def delete_merchant_product_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_categories, merchant_product_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/merchant_product_categories/{id}", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def update_merchant_product_categories_by_id(id: ObjectId, patch: merchant_product_categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_categories, merchant_product_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/offer_campaigns", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def offer_campaign(tree: offer_campaigns,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/offer_campaigns", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def offer_campaign(tree: offer_campaigns,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/offer_campaigns",response_model= List[offer_campaigns],tags = ["offer_campaigns"])
async def get_offer_campaigns(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(offer_campaigns)
    return trees

@app.get("/offer_campaigns/{id}", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def get_offer_campaigns_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaigns, offer_campaigns.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaigns/{id}", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def delete_offer_campaigns_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaigns, offer_campaigns.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/offer_campaigns/{id}", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def update_offer_campaigns_by_id(id: ObjectId, patch: offer_campaigns_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaigns, offer_campaigns.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/openid_providers", response_model=openid_providers,tags = ["openid_providers"])
async def openid_provider(tree: openid_providers,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/openid_providers", response_model=openid_providers,tags = ["openid_providers"])
async def openid_provider(tree: openid_providers,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/openid_providers",response_model= List[openid_providers],tags = ["openid_providers"])
async def get_openid_providers(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(openid_providers)
    return trees

@app.get("/openid_provider/{id}", response_model=openid_providers,tags = ["openid_providers"])
async def get_openid_providers_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(openid_providers, openid_providers.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/openid_providers/{id}", response_model=openid_providers,tags = ["openid_providers"])
async def delete_openid_providers_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(openid_providers, openid_providers.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/openid_providers/{id}", response_model=openid_providers,tags = ["openid_providers"])
async def update_openid_providers_by_id(id: ObjectId, patch: openid_providers_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(openid_providers, openid_providers.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

# @app.post("/administrator_access_logs", response_model=administrator_access_logs)
# async def administrator_access_log(tree: administrator_access_logs):
#     await engine.save(tree)
#     return tree

@app.put("/wallet_giftcards", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def wallet_giftcard(tree: wallet_giftcards,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/wallet_giftcards", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def wallet_giftcard(tree: wallet_giftcards,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/wallet_giftcards",response_model= List[wallet_giftcards],tags = ["wallet_giftcards"])
async def get_wallet_giftcards(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(wallet_giftcards)
    return trees

@app.get("/wallet_giftcards/{id}", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def get_wallet_giftcards_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(wallet_giftcards, wallet_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/wallet_giftcards/{id}", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def delete_wallet_giftcards_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(wallet_giftcards, wallet_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/wallet_giftcards/{id}", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def update_wallet_giftcards_by_id(id: ObjectId, patch: wallet_giftcards_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(wallet_giftcards, wallet_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/delivery_methods", response_model=delivery_methods,tags = ["delivery_methods"])
async def delivery_method(tree: delivery_methods,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/delivery_methods", response_model=delivery_methods,tags = ["delivery_methods"])
async def delivery_method(tree: delivery_methods,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/delivery_methods",response_model= List[delivery_methods],tags = ["delivery_methods"])
async def get_delivery_methods(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(delivery_methods)
    return trees

@app.get("/delivery_method/{id}", response_model=delivery_methods,tags = ["delivery_methods"])
async def get_delivery_methods_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(delivery_methods, delivery_methods.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/delivery_methods/{id}", response_model=delivery_methods,tags = ["delivery_methods"])
async def delete_delivery_methods_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(delivery_methods, delivery_methods.id == id)
    if tree is None:
        raise HTTPException(404)
    engine.delete(tree)
    return tree

@app.patch("/delivery_methods/{id}", response_model=delivery_methods,tags = ["delivery_methods"])
async def update_delivery_methods_by_id(id: ObjectId, patch: delivery_methods_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(delivery_methods, delivery_methods.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

# @app.post("/roles", response_model=roles)
# async def role(tree: roles):
#     await engine.save(tree)
#     return tree
# @app.put("/supplier_accounts", response_model=supplier_accounts,tags = ["supplier_accounts"])
# async def supplier_account(tree: supplier_accounts,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     await engine.save(tree)
#     return tree

# @app.post("/supplier_accounts", response_model=supplier_accounts,tags = ["supplier_accounts"])
# async def supplier_account(tree: supplier_accounts,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     await engine.save(tree)
#     return tree

# @app.get("/supplier_accounts",response_model= List[supplier_accounts],tags = ["supplier_accounts"])
# async def get_supplier_accounts(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     trees = await engine.find(supplier_accounts)
#     return trees

# @app.get("/supplier_accounts/{id}", response_model=supplier_accounts,tags = ["supplier_accounts"])
# async def get_supplier_accounts_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     tree =  await engine.find_one(supplier_accounts, supplier_accounts.id == id)
#     if tree is None:
#         raise HTTPException(404)
#     return tree

# @app.delete("/supplier_accounts/{id}", response_model=supplier_accounts,tags = ["supplier_accounts"])
# async def delete_supplier_accounts_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     tree =  await engine.find_one(supplier_accounts, supplier_accounts.id == id)
#     if tree is None:
#         raise HTTPException(404)
#     engine.delete(tree)
#     return tree

# @app.patch("/supplier_accounts/{id}", response_model=supplier_accounts,tags = ["supplier_accounts"])
# async def update_supplier_accounts_by_id(id: ObjectId, patch: supplier_accounts_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     tree =  await engine.find_one(supplier_accounts, supplier_accounts.id == id)
#     if tree is None:
#         raise HTTPException(404)

#     patch_dict = patch.dict(exclude_unset=True)
#     for name, value in patch_dict.items():
#         setattr(tree, name, value)
#     await engine.save(tree)
#     return tree

@app.put("/merchant_product_images", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def merchant_product_image(tree: merchant_product_images,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/merchant_product_images", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def merchant_product_image(tree: merchant_product_images,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/merchant_product_images",response_model= List[merchant_product_images],tags = ["merchant_product_images"])
async def get_merchant_product_images(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(merchant_product_images)
    return trees

@app.get("/merchant_product_images/{id}", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def get_merchant_product_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_images, merchant_product_images.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_images/{id}", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def delete_merchant_product_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_images, merchant_product_images.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/merchant_product_images/{id}", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def update_merchant_product_images_by_id(id: ObjectId, patch: merchant_product_images_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_images, merchant_product_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/wallets", response_model=wallets,tags = ["wallets"])
async def wallet(tree: wallets,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/wallets", response_model=wallets,tags = ["wallets"])
async def wallet(tree: wallets,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/wallets",response_model= List[wallets],tags = ["wallets"])
async def get_wallets(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(wallets)
    return trees

@app.get("/wallets/{id}", response_model=wallets,tags = ["wallets"])
async def get_wallets_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(wallets, wallets.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/wallets/{id}", response_model=wallets,tags = ["wallets"])
async def delete_wallets_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(wallets, wallets.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/wallets/{id}", response_model=wallets,tags = ["wallets"])
async def update_wallets_by_id(id: ObjectId, patch: wallets_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(wallets, wallets.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/whitelisted_proxies", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def whitelisted_proxie(tree: whitelisted_proxies,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/whitelisted_proxies", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def whitelisted_proxie(tree: whitelisted_proxies,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/whitelisted_proxies",response_model= List[whitelisted_proxies],tags = ["whitelisted_proxies"])
async def get_whitelisted_proxies(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(whitelisted_proxies)
    return trees

@app.get("/whitelisted_proxies/{id}", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def get_whitelisted_proxies_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(whitelisted_proxies, whitelisted_proxies.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/whitelisted_proxies/{id}", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def delete_whitelisted_proxies_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(whitelisted_proxies, whitelisted_proxies.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/whitelisted_proxies/{id}", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def update_whitelisted_proxies_by_id(id: ObjectId, patch: whitelisted_proxies_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(whitelisted_proxies, whitelisted_proxies.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcards", response_model=giftcards,tags = ["giftcards"])
async def giftcard(tree: giftcards,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcards", response_model=giftcards,tags = ["giftcards"])
async def giftcard(tree: giftcards,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcards",response_model= List[giftcards],tags = ["giftcards"])
async def get_giftcards(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcards)
    return trees

@app.get("/giftcard/{id}", response_model=giftcards,tags = ["giftcards"])
async def get_giftcards_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcards, giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcards/{id}", response_model=giftcards,tags = ["giftcards"])
async def delete_giftcards_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcards, giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcards/{id}", response_model=giftcards,tags = ["giftcards"])
async def update_giftcards_by_id(id: ObjectId, patch: giftcards_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcards, giftcards.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_terms", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def giftcard_term(tree: giftcard_terms,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_terms", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def giftcard_term(tree: giftcard_terms,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_terms",response_model= List[giftcard_terms],tags = ["giftcard_terms"])
async def get_giftcard_terms(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_terms)
    return trees

@app.get("/giftcard_term/{id}", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def get_giftcard_terms_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_terms, giftcard_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_terms/{id}", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def delete_giftcard_terms_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_terms, giftcard_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_terms/{id}", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def update_giftcard_terms_by_id(id: ObjectId, patch: giftcard_terms_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_terms, giftcard_terms.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/third_party_brands", response_model=third_party_brands, tags = ["third_party_brands"])
async def third_party_brand(tree: third_party_brands,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/third_party_brands", response_model=third_party_brands, tags = ["third_party_brands"])
async def third_party_brand(tree: third_party_brands,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/third_party_brands",response_model= List[third_party_brands],tags = ["third_party_brands"])
async def get_third_party_brands(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(third_party_brands)
    return trees

@app.get("/third_party_brand/{id}", response_model=third_party_brands,tags = ["third_party_brands"])
async def get_third_party_brands_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(third_party_brands, third_party_brands.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/third_party_brands/{id}", response_model=third_party_brands,tags = ["third_party_brands"])
async def delete_third_party_brands_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(third_party_brands, third_party_brands.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/third_party_brands/{id}", response_model=third_party_brands,tags = ["third_party_brands"])
async def update_third_party_brands_by_id(id: ObjectId, patch: third_party_brands_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(third_party_brands, third_party_brands.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_types", response_model=giftcard_types, tags = ["giftcard_types"])
async def giftcard_type(tree: giftcard_types,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_types", response_model=giftcard_types, tags = ["giftcard_types"])
async def giftcard_type(tree: giftcard_types,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_types",response_model= List[giftcard_types],tags = ["giftcard_types"])
async def get_giftcard_types(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_types)
    return trees

@app.get("/giftcard_type/{id}", response_model=giftcard_types,tags = ["giftcard_types"])
async def get_giftcard_types_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_types, giftcard_types.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_types/{id}", response_model=giftcard_types,tags = ["giftcard_types"])
async def delete_giftcard_types_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_types, giftcard_types.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_types/{id}", response_model=giftcard_types,tags = ["giftcard_types"])
async def update_giftcard_types_by_id(id: ObjectId, patch: giftcard_types_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_types, giftcard_types.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree


@app.put("/experience_orders", response_model=experience_orders, tags = ["experience_orders"])
async def experience_order(tree: experience_orders,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/experience_orders", response_model=experience_orders, tags = ["experience_orders"])
async def experience_order(tree: experience_orders,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/experience_orders",response_model= List[experience_orders],tags = ["experience_orders"])
async def get_experience_orders(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(experience_orders)
    return trees

@app.get("/experience_orders/{id}", response_model=experience_orders,tags = ["experience_orders"])
async def get_experience_orders_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(experience_orders, experience_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_orders/{id}", response_model=experience_orders,tags = ["experience_orders"])
async def delete_experience_orders_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_orders, experience_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/experience_orders/{id}", response_model=experience_orders,tags = ["experience_orders"])
async def update_experience_orders_by_id(id: ObjectId, patch: experience_orders_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_orders, experience_orders.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/experience_slots", response_model=experience_slots,tags = ["experience_slots"])
async def experience_slot(tree: experience_slots,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/experience_slots", response_model=experience_slots,tags = ["experience_slots"])
async def experience_slot(tree: experience_slots,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/experience_slots",response_model= List[experience_slots],tags = ["experience_slots"])
async def get_experience_slots(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(experience_slots)
    return trees

@app.get("/experience_slots/{id}", response_model=experience_slots,tags = ["experience_slots"])
async def get_experience_slots_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_slots, experience_slots.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_slots/{id}", response_model=experience_slots,tags = ["experience_slots"])
async def delete_experience_slots_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_slots, experience_slots.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/experience_slots/{id}", response_model=experience_slots,tags = ["experience_slots"])
async def update_experience_slots_by_id(id: ObjectId, patch: experience_slots_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_slots, experience_slots.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/suppliers", response_model=suppliers,tags = ["suppliers"])
async def supplier(tree: suppliers,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/suppliers", response_model=suppliers,tags = ["suppliers"])
async def supplier(tree: suppliers,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/suppliers",response_model= List[suppliers],tags = ["suppliers"])
async def get_suppliers(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(suppliers)
    return trees

@app.get("/supplier/{id}", response_model=suppliers,tags = ["suppliers"])
async def get_suppliers_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(suppliers, suppliers.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/suppliers/{id}", response_model=suppliers,tags = ["suppliers"])
async def delete_suppliers_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(suppliers, suppliers.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/suppliers/{id}", response_model=suppliers,tags = ["suppliers"])
async def update_suppliers_by_id(id: ObjectId, patch: suppliers_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(suppliers, suppliers.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

#######

@app.put("/partner", response_model=partner,tags = ["partner"])
async def put_partner(tree: partner,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/partner", response_model=partner,tags = ["partner"])
async def post_partner(tree: partner,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/partner",response_model= List[partner],tags = ["partner"])
async def get_partner(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(partner)
    return trees

@app.get("/partner/{id}", response_model=partner,tags = ["partner"])
async def get_partner_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(partner, partner.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/partner/{id}", response_model=partner,tags = ["partner"])
async def delete_partner_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(partner, partner.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/partner/{id}", response_model=partner,tags = ["partner"])
async def update_partner_by_id(id: ObjectId, patch: partner_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(partner, partner.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree
#######

@app.put("/supplier_access_logs", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def supplier_access_log(tree: supplier_access_logs,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/supplier_access_logs", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def supplier_access_log(tree: supplier_access_logs,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/supplier_access_logs",response_model= List[supplier_access_logs],tags = ["supplier_access_logs"])
async def get_supplier_access_logs(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(supplier_access_logs)
    return trees

@app.get("/supplier_access_log/{id}", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def get_supplier_access_logs_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(supplier_access_logs, supplier_access_logs.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/supplier_access_logs/{id}", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def delete_supplier_access_logs_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(supplier_access_logs, supplier_access_logs.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/supplier_access_logs/{id}", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def update_supplier_access_logs_by_id(id: ObjectId, patch: supplier_access_logs_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(supplier_access_logs, supplier_access_logs.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/offer_campaign_categories", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def offer_campaign_category(tree: offer_campaign_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/offer_campaign_categories", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def offer_campaign_category(tree: offer_campaign_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/offer_campaign_categories",response_model= List[offer_campaign_categories],tags = ["offer_campaign_categories"])
async def get_offer_campaign_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(offer_campaign_categories)
    return trees

@app.get("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def get_offer_campaign_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def delete_offer_campaign_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def update_offer_campaign_categories_by_id(id: ObjectId, patch: offer_campaign_categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/experience_details", response_model=experience_details,tags = ["experience_details"])
async def experience_detail(tree: experience_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/experience_details", response_model=experience_details,tags = ["experience_details"])
async def experience_detail(tree: experience_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/experience_details",response_model= List[experience_details],tags = ["experience_details"])
async def get_experience_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(experience_details)
    return trees

@app.get("/experience_detail/{id}", response_model=experience_details,tags = ["experience_details"])
async def get_experience_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_details, experience_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_details/{id}", response_model=experience_details,tags = ["experience_details"])
async def delete_experience_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_details, experience_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/experience_details/{id}", response_model=experience_details,tags = ["experience_details"])
async def update_experience_details_by_id(id: ObjectId, patch: experience_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_details, experience_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/experience_order_recipients", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def experience_order_recipient(tree: experience_order_recipients,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/experience_order_recipients", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def experience_order_recipient(tree: experience_order_recipients,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/experience_order_recipients",response_model= List[experience_order_recipients],tags = ["experience_order_recipients"])
async def get_experience_order_recipients(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(experience_order_recipients)
    return trees

@app.get("/experience_order_recipient/{id}", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def get_experience_order_recipients_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_order_recipients, experience_order_recipients.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_order_recipients/{id}", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def delete_experience_order_recipients_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_order_recipients, experience_order_recipients.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/experience_order_recipients/{id}", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def update_experience_order_recipients_by_id(id: ObjectId, patch: experience_order_recipients_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_order_recipients, experience_order_recipients.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree


@app.put("/giftcard_styles", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def giftcard_style(tree: giftcard_styles,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_styles", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def giftcard_style(tree: giftcard_styles,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_styles",response_model= List[giftcard_styles],tags = ["giftcard_styles"])
async def get_giftcard_styles(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_styles)
    return trees

@app.get("/giftcard_style/{id}", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def get_giftcard_styles_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(giftcard_styles, giftcard_styles.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_styles/{id}", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def delete_giftcard_styles_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_styles, giftcard_styles.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_styles/{id}", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def update_giftcard_styles_by_id(id: ObjectId, patch: giftcard_styles_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_styles, giftcard_styles.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/experience_images", response_model=experience_images,tags = ["experience_images"])
async def experience_image(tree: experience_images,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/experience_images", response_model=experience_images,tags = ["experience_images"])
async def experience_image(tree: experience_images,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/experience_images",response_model= List[experience_images],tags = ["experience_images"])
async def get_experience_images(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(experience_images)
    return trees

@app.get("/experience_image/{id}", response_model=experience_images,tags = ["experience_images"])
async def get_experience_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_images, experience_images.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_images/{id}", response_model=experience_images,tags = ["experience_images"])
async def delete_experience_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_styles, giftcard_styles.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/experience_images/{id}", response_model=experience_images,tags = ["experience_images"])
async def update_experience_images_by_id(id: ObjectId, patch: experience_images_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(experience_images, experience_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree


@app.put("/variants", response_model=variants,tags = ["variants"])
async def variant(tree: variants,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/variants", response_model=variants,tags = ["variants"])
async def variant(tree: variants,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/variants",response_model= List[variants],tags = ["variants"])
async def get_variants(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(variants)
    return trees

@app.get("/variant/{id}", response_model=variants,tags = ["variants"])
async def get_variants_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(variants, variants.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/variants/{id}", response_model=variants,tags = ["variants"])
async def delete_variants_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(variants, variants.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/variants/{id}", response_model=variants,tags = ["variants"])
async def update_variants_by_id(id: ObjectId, patch: variants_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(variants, variants.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_attributes", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def giftcard_attribute(tree: giftcard_attributes,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_attributes", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def giftcard_attribute(tree: giftcard_attributes,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_attributes",response_model= List[giftcard_attributes],tags = ["giftcard_attributes"])
async def get_giftcard_attributes(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_attributes)
    return trees

@app.get("/giftcard_attribute/{id}", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def get_giftcard_attributes_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_attributes, giftcard_attributes.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_attributes/{id}", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def delete_variants_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_attributes, giftcard_attributes.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_attributes/{id}", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def update_giftcard_attributes_by_id(id: ObjectId, patch: giftcard_attributes_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_attributes, giftcard_attributes.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/user_phones", response_model=user_phones,tags = ["user_phones"])
async def user_phone(tree: user_phones,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/user_phones", response_model=user_phones,tags = ["user_phones"])
async def user_phone(tree: user_phones,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/user_phones",response_model= List[user_phones],tags = ["user_phones"])
async def get_user_phones(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(user_phones)
    return trees

@app.get("/user_phone/{id}", response_model=user_phones,tags = ["user_phones"])
async def get_user_phones_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(user_phones, user_phones.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_phones/{id}", response_model=user_phones,tags = ["user_phones"])
async def delete_user_phones_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_phones, user_phones.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/user_phones/{id}", response_model=user_phones,tags = ["user_phones"])
async def update_user_phones_by_id(id: ObjectId, patch: user_phones_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_phones, user_phones.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/experience_prices", response_model=experience_prices,tags = ["offer_campaign_categories"])
async def experience_price(tree: experience_prices,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

    
@app.post("/experience_prices", response_model=experience_prices,tags = ["offer_campaign_categories"])
async def experience_price(tree: experience_prices,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/offer_campaign_categories",response_model= List[offer_campaign_categories],tags = ["offer_campaign_categories"])
async def get_offer_campaign_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(offer_campaign_categories)
    return trees

@app.get("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def get_offer_campaign_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def delete_offer_campaign_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def update_offer_campaign_categories_by_id(id: ObjectId, patch: offer_campaign_categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/brands", response_model=brands,tags = ["brands"])
async def brand(tree: brands,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/brands", response_model=brands,tags = ["brands"])
async def brand(tree: brands,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/brands",response_model= List[brands],tags = ["brands"])
async def get_brands(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(brands)
    return trees

@app.get("/brands/{id}", response_model=brands,tags = ["brands"])
async def get_brands_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(brands, brands.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/brands/{id}", response_model=brands,tags = ["brands"])
async def delete_brands_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(brands, brands.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/brands/{id}", response_model=brands,tags = ["brands"])
async def update_brands_by_id(id: ObjectId, patch: brands_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(brands, brands.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/offer_campaign_terms", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def offer_campaign_term(tree: offer_campaign_terms,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/offer_campaign_terms", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def offer_campaign_term(tree: offer_campaign_terms,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/offer_campaign_terms",response_model= List[offer_campaign_terms],tags = ["offer_campaign_terms"])
async def get_offer_campaign_terms(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(offer_campaign_terms)
    return trees

@app.get("/offer_campaign_terms/{id}", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def get_offer_campaign_terms_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_terms, offer_campaign_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_terms/{id}", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def delete_offer_campaign_terms_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_terms, offer_campaign_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/offer_campaign_terms/{id}", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def update_offer_campaign_terms_by_id(id: ObjectId, patch: offer_campaign_terms_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_terms, offer_campaign_terms.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/interface_methods", response_model=interface_methods,tags = ["interface_methods"])
async def interface_method(tree: interface_methods,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/interface_methods", response_model=interface_methods,tags = ["interface_methods"])
async def interface_method(tree: interface_methods,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/interface_methods",response_model= List[interface_methods],tags = ["interface_methods"])
async def get_offer_campaign_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(interface_methods)
    return trees

@app.get("/interface_methods/{id}", response_model=interface_methods,tags = ["interface_methods"])
async def get_interface_methods_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(interface_methods, interface_methods.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/interface_methods/{id}", response_model=interface_methods,tags = ["interface_methods"])
async def delete_interface_methods_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(interface_methods, interface_methods.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/interface_methods/{id}", response_model=interface_methods,tags = ["interface_methods"])
async def update_interface_methods_by_id(id: ObjectId, patch: interface_methods_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(interface_methods, interface_methods.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/merchant_product_transaction_categories", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def merchant_product_transaction_categorie(tree: merchant_product_transaction_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/merchant_product_transaction_categories", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def merchant_product_transaction_categorie(tree: merchant_product_transaction_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/merchant_product_transaction_categories",response_model= List[merchant_product_transaction_categories],tags = ["merchant_product_transaction_categories"])
async def get_merchant_product_transaction_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(merchant_product_transaction_categories)
    return trees

@app.get("/merchant_product_transaction_categories/{id}", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def get_merchant_product_transaction_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_transaction_categories, merchant_product_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree


@app.delete("/merchant_product_transaction_categories/{id}", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def delete_merchant_product_transaction_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_transaction_categories, merchant_product_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/merchant_product_transaction_categories/{id}", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def update_merchant_product_transaction_categories_by_id(id: ObjectId, patch: merchant_product_transaction_categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_transaction_categories, merchant_product_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_denominations", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def giftcard_denomination(tree: giftcard_denominations,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_denominations", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def giftcard_denomination(tree: giftcard_denominations,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_denominations",response_model= List[giftcard_denominations],tags = ["giftcard_denominations"])
async def get_giftcard_denominations(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_denominations)
    return trees

@app.get("/giftcard_denominations/{id}", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def get_offer_campaign_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(giftcard_denominations, giftcard_denominations.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_denominations/{id}", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def delete_giftcard_denominations_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_denominations, giftcard_denominations.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_denominations/{id}", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def update_giftcard_denominations_by_id(id: ObjectId, patch: giftcard_denominations_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_denominations, giftcard_denominations.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/gifts", response_model=gifts,tags = ["gifts"])
async def gift(tree: gifts,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/gifts", response_model=gifts,tags = ["gifts"])
async def gift(tree: gifts,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/gifts",response_model= List[gifts],tags = ["gifts"])
async def get_gifts(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(gifts)
    return trees

@app.get("/gift/{id}", response_model=gifts,tags = ["gifts"])
async def get_gifts_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(gifts, gifts.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/gifts/{id}", response_model=gifts,tags = ["gifts"])
async def delete_gifts_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(gifts, gifts.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/gifts/{id}", response_model=gifts,tags = ["gifts"])
async def update_gifts_by_id(id: ObjectId, patch: gifts_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(gifts, gifts.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree


@app.put("/merchant_product_variants", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def merchant_product_variant(tree: merchant_product_variants,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/merchant_product_variants", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def merchant_product_variant(tree: merchant_product_variants,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/merchant_product_variants",response_model= List[merchant_product_variants],tags = ["merchant_product_variants"])
async def get_merchant_product_variants(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(merchant_product_variants)
    return trees

@app.get("/merchant_product_variants/{id}", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def get_merchant_product_variants_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_variants, merchant_product_variants.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_variants/{id}", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def delete_merchant_product_variants_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_variants, merchant_product_variants.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/merchant_product_variants/{id}", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def update_merchant_product_variants_by_id(id: ObjectId, patch: merchant_product_variants_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_variants, merchant_product_variants.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/user_order_details_giftcards", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def user_order_details_giftcard(tree: user_order_details_giftcards,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/user_order_details_giftcards", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def user_order_details_giftcard(tree: user_order_details_giftcards,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/user_order_details_giftcards",response_model= List[user_order_details_giftcards],tags = ["user_order_details_giftcards"])
async def get_user_order_details_giftcards(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(user_order_details_giftcards)
    return trees

@app.get("/user_order_details_giftcards/{id}", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def get_user_order_details_giftcards_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_order_details_giftcards, user_order_details_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_order_details_giftcards/{id}", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def delete_user_order_details_giftcards_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_order_details_giftcards, user_order_details_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    engine.delete(tree)
    return tree

@app.patch("/user_order_details_giftcards/{id}", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def update_user_order_details_giftcards_by_id(id: ObjectId, patch: user_order_details_giftcards_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_order_details_giftcards, user_order_details_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/user_addresses", response_model=user_addresses,tags = ["user_addresses"])
async def put_user_address(tree: user_addresses,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/user_addresses", response_model=user_addresses,tags = ["user_addresses"])
async def post_user_address(tree: user_addresses,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/user_addresses",response_model= List[user_addresses],tags = ["user_addresses"])
async def get_user_addresses(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(user_addresses)
    return trees

@app.get("/user_addresses/{id}", response_model=user_addresses,tags = ["user_addresses"])
async def get_user_addresses_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_addresses, user_addresses.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_addresses/{id}", response_model=user_addresses,tags = ["user_addresses"])
async def delete_user_addresses_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_addresses, user_addresses.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/user_addresses/{id}", response_model=user_addresses,tags = ["user_addresses"])
async def update_user_addresses_by_id(id: ObjectId, patch: user_addresses_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_addresses, user_addresses.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

# @app.post("/user_credit_cards", response_model=user_credit_cards)
# async def user_credit_card(tree: user_credit_cards,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     await engine.save(tree)
#     return tree

@app.put("/countries", response_model=countries,tags = ["countries"])
async def create_tree(tree: countries,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/countries", response_model=countries,tags = ["countries"])
async def create_tree(tree: countries,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/countries",response_model= List[countries],tags = ["countries"])
async def get_countries(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(countries)
    return trees

@app.get("/countries/{id}", response_model=countries,tags = ["countries"])
async def get_countries_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(countries, countries.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/countries/{id}", response_model=countries,tags = ["countries"])
async def delete_countries_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(countries, countries.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/countries/{id}", response_model=countries,tags = ["countries"])
async def update_countries_by_id(id: ObjectId, patch: countries_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(countries, countries.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/categories", response_model=categories,tags = ["categories"])
async def put_category(tree: categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/categories", response_model=categories,tags = ["categories"])
async def post_category(tree: categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/categories",response_model= List[categories],tags = ["categories"])
async def get_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(categories)
    return trees

@app.get("/offer_campaign_categories/{id}", response_model=categories,tags = ["categories"])
async def get_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(categories, categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/categories/{id}", response_model=categories,tags = ["categories"])
async def delete_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(categories, categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/categories/{id}", response_model=categories,tags = ["categories"])
async def update_categories_by_id(id: ObjectId, patch: categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(categories, categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/redemption_partners", response_model=redemption_partners,tags = ["redemption_partners"])
async def redemption_partner(tree: redemption_partners,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/redemption_partners", response_model=redemption_partners,tags = ["redemption_partners"])
async def redemption_partner(tree: redemption_partners,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/redemption_partners",response_model= List[redemption_partners],tags = ["redemption_partners"])
async def get_redemption_partners(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(redemption_partners)
    return trees

@app.get("/redemption_partners/{id}", response_model=redemption_partners,tags = ["redemption_partners"])
async def get_redemption_partners_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(redemption_partners, redemption_partners.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree


@app.delete("/redemption_partners/{id}", response_model=redemption_partners,tags = ["redemption_partners"])
async def delete_redemption_partners_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(redemption_partners, redemption_partners.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/redemption_partners/{id}", response_model=redemption_partners,tags = ["redemption_partners"])
async def update_redemption_partners_by_id(id: ObjectId, patch: redemption_partners_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(redemption_partners, redemption_partners.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/user_openids", response_model=user_openids,tags = ["user_openids"])
async def user_openid(tree: user_openids,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/user_openids", response_model=user_openids,tags = ["user_openids"])
async def user_openid(tree: user_openids,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/user_openids",response_model= List[user_openids],tags = ["user_openids"])
async def get_user_openids(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(user_openids)
    return trees

@app.get("/user_openids/{id}", response_model=user_openids,tags = ["user_openids"])
async def get_user_openids_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(user_openids, user_openids.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_openids/{id}", response_model=user_openids,tags = ["user_openids"])
async def delete_user_openids_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_openids, user_openids.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/user_openids/{id}", response_model=user_openids,tags = ["user_openids"])
async def update_user_openids_by_id(id: ObjectId, patch: user_openids_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_openids, user_openids.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/transaction_categories", response_model=transaction_categories,tags = ["transaction_categories"])
async def transaction_categorie(tree: transaction_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/transaction_categories", response_model=transaction_categories,tags = ["transaction_categories"])
async def transaction_categorie(tree: transaction_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/transaction_categories",response_model= List[transaction_categories],tags = ["transaction_categories"])
async def get_transaction_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(transaction_categories)
    return trees

@app.get("/transaction_categories/{id}", response_model=transaction_categories,tags = ["transaction_categories"])
async def get_transaction_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(transaction_categories, transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/transaction_categories/{id}", response_model=transaction_categories,tags = ["transaction_categories"])
async def delete_transaction_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(transaction_categories, transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/transaction_categories/{id}", response_model=transaction_categories,tags = ["transaction_categories"])
async def update_transaction_categories_by_id(id: ObjectId, patch: transaction_categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(transaction_categories, transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_batch_giftcard_details", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def giftcard_batch_giftcard_detail(tree: giftcard_batch_giftcard_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_batch_giftcard_details", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def giftcard_batch_giftcard_detail(tree: giftcard_batch_giftcard_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_batch_giftcard_details",response_model= List[giftcard_batch_giftcard_details],tags = ["giftcard_batch_giftcard_details"])
async def get_giftcard_batch_giftcard_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_batch_giftcard_details)
    return trees

@app.get("/giftcard_batch_giftcard_details/{id}", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def get_giftcard_batch_giftcard_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_batch_giftcard_details, giftcard_batch_giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_batch_giftcard_details/{id}", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def delete_giftcard_batch_giftcard_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_batch_giftcard_details, giftcard_batch_giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_batch_giftcard_details/{id}", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def update_giftcard_batch_giftcard_details_by_id(id: ObjectId, patch: giftcard_batch_giftcard_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_batch_giftcard_details, giftcard_batch_giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_variety_denominations", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def giftcard_variety_denomination(tree: giftcard_variety_denominations,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_variety_denominations", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def giftcard_variety_denomination(tree: giftcard_variety_denominations,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_variety_denominations",response_model= List[giftcard_variety_denominations],tags = ["giftcard_variety_denominations"])
async def get_giftcard_variety_denominations(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_variety_denominations)
    return trees

@app.get("/giftcard_variety_denominations/{id}", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def get_giftcard_variety_denominations_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_variety_denominations, giftcard_variety_denominations.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_variety_denominations/{id}", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def delete_giftcard_variety_denominations_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_variety_denominations, giftcard_variety_denominations.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_variety_denominations/{id}", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def update_giftcard_variety_denominations_by_id(id: ObjectId, patch: giftcard_variety_denominations_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_variety_denominations, giftcard_variety_denominations.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

# @app.put("/partner", response_model=partner,tags = ["partner"])
# async def create_partner(tree: partner,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     await engine.save(tree)
#     return tree

# @app.post("/partner", response_model=partner,tags = ["partner"])
# async def create_partner(tree: partner,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     await engine.save(tree)
#     return tree

# @app.get("/partner",response_model= List[partner],tags = ["partner"])
# async def get_partner(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     trees = await engine.find(partner)
#     return trees

# @app.get("/partner/{id}", response_model=partner,tags = ["partner"])
# async def get_partner_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
#     tree =  await engine.find_one(partner, partner.id == id)
#     if tree is None:
#         raise HTTPException(404)
#     return tree

# @app.delete("/partner/{id}", response_model=partner,tags = ["partner"])
# async def delete_partner_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     tree =  await engine.find_one(partner, partner.id == id)
#     if tree is None:
#         raise HTTPException(404)
#     await engine.delete(tree)
#     return tree

# @app.patch("/partner/{id}", response_model=partner,tags = ["partner"])
# async def update_partner_by_id(id: ObjectId, patch: partner_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
#     tree =  await engine.find_one(partner, partner.id == id)
#     if tree is None:
#         raise HTTPException(404)

#     patch_dict = patch.dict(exclude_unset=True)
#     for name, value in patch_dict.items():
#         setattr(tree, name, value)
#     await engine.save(tree)
#     return tree

@app.put("/giftcard_details", response_model=giftcard_details,tags = ["giftcard_details"])
async def giftcard_detail(tree: giftcard_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_details", response_model=giftcard_details,tags = ["giftcard_details"])
async def giftcard_detail(tree: giftcard_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_details",response_model= List[giftcard_details],tags = ["giftcard_details"])
async def get_giftcard_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_details)
    return trees

@app.get("/giftcard_detail/{id}", response_model=giftcard_details,tags = ["giftcard_details"])
async def get_giftcard_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_details, giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_details/{id}", response_model=giftcard_details,tags = ["giftcard_details"])
async def delete_users_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_details, giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_details/{id}", response_model=giftcard_details,tags = ["giftcard_details"])
async def update_giftcard_details_by_id(id: ObjectId, patch: giftcard_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_details, giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/third_party_order_details", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def third_party_order_detail(tree: third_party_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/third_party_order_details", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def third_party_order_detail(tree: third_party_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/third_party_order_details",response_model= List[third_party_order_details],tags = ["third_party_order_details"])
async def get_third_party_order_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(third_party_order_details)
    return trees

@app.get("/third_party_order_details/{id}", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def get_third_party_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(third_party_order_details, third_party_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/third_party_order_details/{id}", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def delete_users_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(third_party_order_details, third_party_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/third_party_order_details/{id}", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def update_third_party_order_details_by_id(id: ObjectId, patch: third_party_order_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(third_party_order_details, third_party_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/user_orders", response_model=user_orders,tags = ["user_orders"])
async def user_order(tree: user_orders,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/user_orders", response_model=user_orders,tags = ["user_orders"])
async def user_order(tree: user_orders,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/user_orders",response_model= List[user_orders],tags = ["user_orders"])
async def get_user_orders(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(user_orders)
    return trees

@app.get("/user_orders/{id}", response_model=user_orders,tags = ["user_orders"])
async def get_user_orders_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(user_orders, user_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_orders/{id}", response_model=user_orders,tags = ["user_orders"])
async def delete_user_orders_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_orders, user_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/user_orders/{id}", response_model=user_orders,tags = ["user_orders"])
async def update_user_orders_by_id(id: ObjectId, patch: user_orders_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_orders, user_orders.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/offer_order_details", response_model=offer_order_details,tags = ["offer_order_details"])
async def offer_order_detail(tree: offer_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/offer_order_details", response_model=offer_order_details,tags = ["offer_order_details"])
async def offer_order_detail(tree: offer_order_details,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/offer_order_details",response_model= List[offer_order_details],tags = ["offer_order_details"])
async def get_offer_order_details(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(offer_order_details)
    return trees

@app.get("/offer_order_details/{id}", response_model=offer_order_details,tags = ["offer_order_details"])
async def get_offer_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_order_details, offer_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_order_details/{id}", response_model=offer_order_details,tags = ["offer_order_details"])
async def delete_offer_order_details_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_order_details, offer_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/offer_order_details/{id}", response_model=offer_order_details,tags = ["offer_order_details"])
async def update_offer_order_details_by_id(id: ObjectId, patch: offer_order_details_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_order_details, offer_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_style_images", response_model=giftcard_style_images,tags = ["giftcard_style_images"])
async def giftcard_style_image(tree: giftcard_style_images,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_style_images", response_model=giftcard_style_images,tags = ["giftcard_style_images"])
async def giftcard_style_image(tree: giftcard_style_images,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_style_images",response_model= List[giftcard_style_images],tags = ["giftcard_style_images"])
async def get_giftcard_style_images(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_style_images)
    return trees

@app.get("/giftcard_style_images/{id}", response_model=giftcard_style_images,tags = ["giftcard_style_images"])
async def get_giftcard_style_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(giftcard_style_images, giftcard_style_images.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_style_images/{id}", response_model=giftcard_style_images,tags = ["giftcard_style_images"])
async def delete_giftcard_style_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_style_images, giftcard_style_images.id == id)
    if tree is None:
        raise HTTPException(404)
    engine.delete(tree)
    return tree

@app.patch("/giftcard_style_images/{id}", response_model=giftcard_style_images, tags = ["giftcard_style_images"])
async def update_giftcard_style_images_by_id(id: ObjectId, patch: giftcard_style_images_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_style_images, giftcard_style_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/merchant_product_terms", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def merchant_product_term(tree: merchant_product_terms,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/merchant_product_terms", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def merchant_product_term(tree: merchant_product_terms,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/merchant_product_terms",response_model= List[merchant_product_terms],tags = ["merchant_product_terms"])
async def get_merchant_product_terms(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(merchant_product_terms)
    return trees

@app.get("/merchant_product_terms/{id}", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def get_merchant_product_terms_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(merchant_product_terms, merchant_product_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_terms/{id}", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def delete_giftcard_style_images_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_terms, merchant_product_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/merchant_product_terms/{id}", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def update_merchant_product_terms_by_id(id: ObjectId, patch: merchant_product_terms_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_product_terms, merchant_product_terms.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/merchant_products", response_model=merchant_products,tags = ["merchant_products"])
async def merchant_product(tree: merchant_products,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/merchant_products", response_model=merchant_products,tags = ["merchant_products"])
async def merchant_product(tree: merchant_products,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree


@app.get("/merchant_products",response_model= List[merchant_products],tags = ["merchant_products"])
async def get_merchant_products(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(merchant_products)
    return trees

@app.get("/merchant_products/{id}", response_model=merchant_products,tags = ["merchant_products"])
async def get_merchant_products_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_products, merchant_products.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_products/{id}", response_model=merchant_products,tags = ["merchant_products"])
async def delete_merchant_products_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_products, merchant_products.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/merchant_products/{id}", response_model=merchant_products ,tags = ["merchant_products"])
async def update_merchant_products_by_id(id: ObjectId, patch: merchant_products_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(merchant_products, merchant_products.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/variant_values", response_model=variant_values,tags = ["variant_values"])
async def variant_value(tree: variant_values,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/variant_values", response_model=variant_values,tags = ["variant_values"])
async def variant_value(tree: variant_values,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/variant_values",response_model= List[variant_values],tags = ["variant_values"])
async def get_variant_values(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(variant_values)
    return trees

@app.get("/variant_values/{id}", response_model=variant_values,tags = ["variant_values"])
async def get_variant_values_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(variant_values, variant_values.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/variant_values/{id}", response_model=variant_values,tags = ["variant_values"])
async def delete_variant_values_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(variant_values, variant_values.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/variant_values/{id}", response_model=variant_values, tags = ["variant_values"])
async def update_variant_values_by_id(id: ObjectId, patch: variant_values_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(variant_values, variant_values.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/offer_orders", response_model=offer_orders,tags = ["offer_orders"])
async def offer_order(tree: offer_orders,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/offer_orders", response_model=offer_orders,tags = ["offer_orders"])
async def offer_order(tree: offer_orders,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/offer_orders",response_model= List[offer_orders],tags = ["offer_orders"])
async def get_offer_orders(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(offer_orders)
    return trees

@app.get("/offer_orders/{id}", response_model=offer_orders,tags = ["offer_orders"])
async def get_offer_orders_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(offer_orders, offer_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_orders/{id}", response_model=offer_orders,tags = ["offer_orders"])
async def delete_offer_orders_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_orders, offer_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/offer_orders/{id}", response_model=offer_orders, tags = ["offer_orders"])
async def update_offer_orders_by_id(id: ObjectId, patch: offer_orders_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_orders, offer_orders.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/giftcard_varieties", response_model=giftcard_varieties,tags = ["giftcard_varieties"])
async def giftcard_varietie(tree: giftcard_varieties,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/giftcard_varieties", response_model=giftcard_varieties,tags = ["giftcard_varieties"])
async def giftcard_varietie(tree: giftcard_varieties,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/giftcard_varieties",response_model= List[giftcard_varieties],tags = ["giftcard_varieties"])
async def get_giftcard_varieties(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(giftcard_varieties)
    return trees

@app.get("/giftcard_varieties/{id}", response_model=giftcard_varieties,tags = ["giftcard_varieties"])
async def get_giftcard_varieties_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_varieties, giftcard_varieties.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_varieties/{id}", response_model=giftcard_varieties,tags = ["giftcard_varieties"])
async def delete_giftcard_varieties_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_varieties, giftcard_varieties.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/giftcard_varieties/{id}", response_model=giftcard_varieties, tags= ["giftcard_varieties"])
async def update_giftcard_varieties_by_id(id: ObjectId, patch: giftcard_varieties_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(giftcard_varieties, giftcard_varieties.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/schema_migrations", response_model=schema_migrations,tags = ["schema_migrations"])
async def schema_migration(tree: schema_migrations,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/schema_migrations", response_model=schema_migrations,tags = ["schema_migrations"])
async def schema_migration(tree: schema_migrations,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/schema_migrations",response_model= List[schema_migrations],tags = ["schema_migrations"])
async def get_schema_migrations(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(schema_migrations)
    return trees

@app.get("/schema_migration/{id}", response_model=schema_migrations,tags = ["schema_migrations"])
async def get_schema_migrations_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(schema_migrations, schema_migrations.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/schema_migrations/{id}", response_model=schema_migrations,tags = ["schema_migrations"])
async def delete_schema_migrations_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(schema_migrations, schema_migrations.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/schema_migrations/{id}", response_model=schema_migrations, tags= ["schema_migrations"])
async def update_schema_migrations_by_id(id: ObjectId, patch: schema_migrations_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(schema_migrations, schema_migrations.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/offer_campaign_transaction_categories", response_model=offer_campaign_transaction_categories ,tags = ["offer_campaign_transaction_categories"])
async def offer_campaign_transaction_categorie(tree: offer_campaign_transaction_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/offer_campaign_transaction_categories", response_model=offer_campaign_transaction_categories ,tags = ["offer_campaign_transaction_categories"])
async def offer_campaign_transaction_categorie(tree: offer_campaign_transaction_categories,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/offer_campaign_transaction_categories",response_model= List[offer_campaign_transaction_categories],tags = ["offer_campaign_transaction_categories"])
async def get_offer_campaign_transaction_categories(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(offer_campaign_transaction_categories)
    return trees

@app.get("/offer_campaign_transaction_category/{id}", response_model=offer_campaign_transaction_categories,tags = ["offer_campaign_transaction_categories"])
async def get_offer_campaign_transaction_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_transaction_categories, offer_campaign_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_transaction_categories/{id}", response_model=offer_campaign_transaction_categories,tags = ["offer_campaign_transaction_categories"])
async def delete_offer_campaign_transaction_categories_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_transaction_categories, offer_campaign_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/offer_campaign_transaction_categories/{id}", response_model=offer_campaign_transaction_categories, tags= ["offer_campaign_transaction_categories"])
async def update_offer_campaign_transaction_categories_by_id(id: ObjectId, patch: offer_campaign_transaction_categories_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(offer_campaign_transaction_categories, offer_campaign_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/normalized_addresses", response_model=normalized_addresses,tags = ["normalized_addresses"])
async def normalized_addresse(tree: normalized_addresses,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/normalized_addresses", response_model=normalized_addresses,tags = ["normalized_addresses"])
async def normalized_addresse(tree: normalized_addresses,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/normalized_addresses",response_model= List[normalized_addresses],tags = ["normalized_addresses"])
async def get_normalized_addresses(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(normalized_addresses)
    return trees

@app.get("/offer_campaign_transaction_categories/{id}", response_model=normalized_addresses,tags = ["normalized_addresses"])
async def get_normalized_addresses_by_id(id: ObjectId, form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(normalized_addresses, normalized_addresses.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/normalized_addresses/{id}", response_model=normalized_addresses,tags = ["normalized_addresses"])
async def delete_normalized_addresses_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(normalized_addresses, normalized_addresses.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/normalized_addresses/{id}", response_model=normalized_addresses, tags= ["normalized_addresses"])
async def update_normalized_addresses_by_id(id: ObjectId, patch: normalized_addresses_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(normalized_addresses, normalized_addresses.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

@app.put("/user_emails", response_model=user_emails,tags = ["user_emails"])
async def user_email(tree: user_emails,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.post("/user_emails", response_model=user_emails,tags = ["user_emails"])
async def user_email(tree: user_emails,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    await engine.save(tree)
    return tree

@app.get("/user_emails",response_model= List[user_emails],tags = ["user_emails"])
async def get_user_emails(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(user_emails)
    return trees

@app.get("/user_emails/{id}", response_model=user_emails,tags = ["user_emails"])
async def get_user_emails_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper) ):
    tree =  await engine.find_one(user_emails, user_emails.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_emails/{id}", response_model=user_emails,tags = ["user_emails"])
async def delete_user_emails_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_emails, user_emails.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

@app.patch("/user_emails/{id}", response_model=user_emails, tags= ["user_emails"])
async def update_user_emails_by_id(id: ObjectId, patch: user_emails_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree =  await engine.find_one(user_emails, user_emails.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

# @app.post("/user_phone_logins", response_model=user_phone_logins)
# async def user_phone_login(tree: user_phone_logins):
#     await engine.save(tree)
#     return tree

# @app.post("/role_entitlements", response_model=role_entitlements)
# async def role_entitlement(tree: role_entitlements):
#     await engine.save(tree)
#     return tree

# @app.post("/administrator_activity_logs", response_model=administrator_activity_logs)
# async def administrator_activity_log(tree: administrator_activity_logs):
#     await engine.save(tree)
#     return tree

# @app.post("/user_logins", response_model=user_logins)
# async def user_login(tree: user_logins):
#     await engine.save(tree)
#     return tree

# @app.post("/user_activity_logs", response_model=user_activity_logs)
# async def user_activity_log(tree: user_activity_logs):
#     await engine.save(tree)
#     return tree

# @app.post("/User_access_logs", response_model=User_access_logs)
# async def User_access_log(tree: User_access_logs):
#     await engine.save(tree)
#     return tree

# @app.post("/administrators", response_model=administrators)
# async def administrator(tree: administrators):
#     await engine.save(tree)
#     return tree

# @app.post("/administrator_roles", response_model=administrator_roles)
# async def administrator_role(tree: administrator_roles):
#     await engine.save(tree)
#     return tree


# @app.post("/user_tokens", response_model=user_tokens)
# async def user_token(tree: user_tokens):
#     await engine.save(tree)
#     return tree

