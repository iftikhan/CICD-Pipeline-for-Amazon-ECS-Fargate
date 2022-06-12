from fastapi import FastAPI, HTTPException, File, UploadFile
from typing import Collection, List
from fastapi.param_functions import Depends, Form
from odmantic.bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

from backend.model import (Merchant_product_details,giftcard_attribute_values,merchant_product_orders,
                    brand_categories,brand_category_transaction_categories,user_order_details,merchant_product_detail_variant_values,
                    brand_images,giftcard_batches,giftcard_variety_brands,merchant_product_order_details,experience_order_details,homepage_banners,
                    point_transactions,offer_campaign_images,giftcard_units,merchant_product_categories,offer_campaigns, openid_providers,
                    wallet_giftcards,delivery_methods,supplier_accounts,merchant_product_images,wallets,whitelisted_proxies,giftcards,giftcard_terms,third_party_brands,giftcard_types,experience_orders,experience_slots,
                    suppliers,supplier_access_logs,offer_campaign_categories,experience_details,experience_order_recipients,variant_values,
                    giftcard_styles,experience_images,variants,giftcard_attributes,user_phones,experience_prices,brands,offer_campaign_terms,merchant_product_terms,merchant_product_transaction_categories,
                    merchant_product_variants,merchant_products,interface_methods,offer_campaign_transaction_categories,offer_order_details,offer_orders,giftcard_batch_giftcard_details,
                    giftcard_denominations,giftcard_details,giftcard_style_images,giftcard_varieties,giftcard_variety_denominations,gifts,user_order_details_giftcards,user_addresses,
                    user_emails,user_openids,user_orders,users,categories,redemption_partners,countries, transaction_categories,third_party_order_details,schema_migrations,normalized_addresses)


from backend.model_update import (Merchant_product_details_update,giftcard_attribute_values_update,merchant_product_orders_update,
                    brand_categories_update,brand_category_transaction_categories_update,user_order_details_update,merchant_product_detail_variant_values_update,
                    brand_images_update,giftcard_batches_update,giftcard_variety_brands_update,merchant_product_order_details_update,experience_order_details_update,homepage_banners_update,
                    point_transactions_update,offer_campaign_images_update,giftcard_units_update,merchant_product_categories_update,offer_campaigns_update, openid_providers_update,
                    wallet_giftcards_update,delivery_methods_update,supplier_accounts_update,merchant_product_images_update,wallets_update,whitelisted_proxies_update,giftcards_update,giftcard_terms_update,third_party_brands_update,giftcard_types_update,experience_orders_update,experience_slots_update,
                    suppliers_update,supplier_access_logs_update,offer_campaign_categories_update,experience_details_update,experience_order_recipients_update,variant_values_update,
                    giftcard_styles_update,experience_images_update,variants_update,giftcard_attributes_update,user_phones_update,brands_update,offer_campaign_terms_update,merchant_product_terms_update,merchant_product_transaction_categories_update,
                    merchant_product_variants_update,merchant_products_update,interface_methods_update,offer_campaign_transaction_categories_update,offer_order_details_update,offer_orders_update,giftcard_batch_giftcard_details_update,
                    giftcard_denominations_update,giftcard_details_update,giftcard_style_images_update,giftcard_varieties_update,giftcard_variety_denominations_update,gifts_update,user_order_details_giftcards_update,user_addresses_update,
                    user_emails_update,user_openids_update,user_orders_update,users_update,categories_update,redemption_partners_update,countries_update, transaction_categories_update,third_party_order_details_update,schema_migrations_update,normalized_addresses_update)


import motor
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import json
from database.database import Db
from login.auth import AuthHandler
from fastapi.security import OAuth2PasswordRequestForm

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


print(Db.client)

app.add_middleware(CORSMiddleware,    allow_origins=["*"],    allow_methods=["*"],    allow_headers=["*"],    allow_credentials=True )
auth_handler = AuthHandler()


@app.post("/Merchant_product_details", response_model=Merchant_product_details, tags = ["Merchant_product_details"])
async def Merchant_product_detail(tree: Merchant_product_details, db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/merchant_product_details",response_model= List[Merchant_product_details],tags = ["Merchant_product_details"])
async def get_merchant_product_details(db: AsyncIOMotorClient = Depends(Db),form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await db.engine.find(Merchant_product_details)
    return trees

@app.get("/merchant_product_details/{id}", response_model=Merchant_product_details,tags = ["Merchant_product_details"])
async def get_tree_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db),form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await db.engine.find_one(Merchant_product_details, Merchant_product_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_detail/{id}", response_model=Merchant_product_details,tags = ["Merchant_product_details"])
async def delete_merchant_product_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(Merchant_product_details, Merchant_product_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_detail/{id}", response_model=Merchant_product_details,tags = ["Merchant_product_details"])
async def update_merchant_product_detail_by_id(id: ObjectId, patch: Merchant_product_details_update, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(Merchant_product_details, Merchant_product_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcard_attribute_values", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def giftcard_attribute_value(tree: giftcard_attribute_values, db: AsyncIOMotorClient = Depends(Db)):
    db.engine.save(tree)
    return tree

@app.get("/giftcard_attribute_values",response_model= List[giftcard_attribute_values],tags = ["giftcard_attribute_values"])
async def get_giftcard_attribute_values( db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_attribute_values)
    return trees

@app.get("/giftcard_attribute_values/{id}", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def get_giftcard_attribute_values_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_attribute_values, giftcard_attribute_values.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_attribute_value/{id}", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def delete_giftcard_attribute_values_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_attribute_values, giftcard_attribute_values.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_attribute_values/{id}", response_model=giftcard_attribute_values,tags = ["giftcard_attribute_values"])
async def update_giftcard_attribute_values_by_id(id: ObjectId, patch: giftcard_attribute_values_update, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_attribute_values, giftcard_attribute_values.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/merchant_product_orders", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def merchant_product_order(tree: merchant_product_orders, db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/merchant_product_orders",response_model= List[merchant_product_orders],tags = ["merchant_product_orders"])
async def get_merchant_product_orders( db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_product_orders)
    return trees

@app.get("/merchant_product_orders/{id}", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def get_merchant_product_orders_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_orders, merchant_product_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_orders/{id}", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def delete_merchant_product_orders_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_orders, merchant_product_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_orders/{id}", response_model=merchant_product_orders,tags = ["merchant_product_orders"])
async def update_merchant_product_orders_by_id(id: ObjectId, patch: merchant_product_orders_update,  db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_orders, merchant_product_orders.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/brand_categories", response_model=brand_categories,tags = ["brand_categories"])
async def brand_categorie(tree: brand_categories, db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/brand_categories",response_model= List[brand_categories],tags = ["brand_categories"])
async def get_brand_categories( db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(brand_categories)
    return trees

@app.get("/brand_category_by/{id}", response_model=brand_categories,tags = ["brand_categories"])
async def get_brand_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_categories, brand_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/brand_categories/{id}", response_model=brand_categories,tags = ["brand_categories"])
async def delete_brand_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_categories, brand_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/brand_categories/{id}", response_model=brand_categories,tags = ["brand_categories"])
async def update_brand_categories_by_id(id: ObjectId, patch: brand_categories_update, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_categories, brand_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/brand_category_transaction_categories", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def brand_category_transaction_categorie(tree: brand_category_transaction_categories, db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/brand_category_transaction_categories",response_model= List[brand_category_transaction_categories],tags = ["brand_category_transaction_categories"])
async def get_brand_category_transaction_categoriess( db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(brand_category_transaction_categories)
    return trees

@app.get("/brand_categories/{id}", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def get_brand_category_transaction_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_category_transaction_categories, brand_category_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/brand_category_transaction_categories/{id}", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def delete_brand_category_transaction_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_category_transaction_categories, brand_category_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/brand_category_transaction_categories/{id}", response_model=brand_category_transaction_categories,tags = ["brand_category_transaction_categories"])
async def update_brand_category_transaction_categories_by_id(id: ObjectId, patch: brand_category_transaction_categories_update, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_category_transaction_categories, brand_category_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/user_order_details", response_model=user_order_details,tags = ["user_order_details"])
async def user_order_detail(tree: user_order_details, db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/user_order_details",response_model= List[user_order_details],tags = ["user_order_details"])
async def get_user_order_details(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(user_order_details)
    return trees

@app.get("/user_order_details/{id}", response_model=user_order_details,tags = ["user_order_details"])
async def get_user_order_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_order_details, user_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_order_details/{id}", response_model=user_order_details,tags = ["user_order_details"])
async def delete_user_order_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_order_details, user_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/user_order_details/{id}", response_model=user_order_details,tags = ["user_order_details"])
async def update_user_order_details_by_id(id: ObjectId, patch: user_order_details_update,  db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_order_details, user_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/merchant_product_detail_variant_values", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def merchant_product_detail_variant(tree: merchant_product_detail_variant_values, db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/merchant_product_detail_variant_values",response_model= List[merchant_product_detail_variant_values],tags = ["merchant_product_detail_variant_values"])
async def get_brand_categories( db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_product_detail_variant_values)
    return trees

@app.get("/merchant_product_detail_variant_values/{id}", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def get_merchant_product_detail_variant_values_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_detail_variant_values, merchant_product_detail_variant_values.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_detail_variant_values/{id}", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def delete_merchant_product_detail_variant_values_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_detail_variant_values, merchant_product_detail_variant_values.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_detail_variant_values/{id}", response_model=merchant_product_detail_variant_values,tags = ["merchant_product_detail_variant_values"])
async def update_merchant_product_detail_variant_values_by_id(id: ObjectId, patch: merchant_product_detail_variant_values_update, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_detail_variant_values, merchant_product_detail_variant_values.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/brand_images", response_model=brand_images,tags = ["brand_images"])
async def brand_image(tree: brand_images, file : UploadFile = Form(...), db: AsyncIOMotorClient = Depends(Db)):
    tree['image'] = file
    await db.engine.save_all(tree)
    return tree

@app.get("/brand_images",response_model= List[brand_images],tags = ["brand_images"])
async def get_brand_images( db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(brand_images)
    return trees

@app.get("/brand_images/{id}", response_model=brand_images,tags = ["brand_images"])
async def get_brand_images_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_images, brand_images.id == id)
    if tree is None:
        raise HTTPException(404, detail= "ObjectID Not available")
    return tree

@app.delete("/brand_image/{id}", response_model=brand_images,tags = ["brand_images"])
async def delete_brand_images_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_images, brand_images.id == id)
    if tree is None:
        raise HTTPException(status_code= 404, detail= "ObjectID Not available")
    await db.engine.delete(tree)
    return tree

@app.patch("/brand_images/{id}", response_model=brand_images,tags = ["brand_images"])
async def update_brand_images_by_id(id: ObjectId, patch: brand_images_update, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brand_images, brand_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
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


@app.post("/giftcard_batches", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def giftcard_batche(tree: giftcard_batches, db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_batches",response_model= List[giftcard_batches],tags = ["giftcard_batches"])
async def get_giftcard_batches(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_batches)
    return trees

@app.get("/giftcard_batches/{id}", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def get_giftcard_batches_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_batches, giftcard_batches.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_batches/{id}", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def delete_giftcard_batches_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_batches, giftcard_batches.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_batches/{id}", response_model=giftcard_batches,tags = ["giftcard_batches"])
async def update_giftcard_batches_by_id(id: ObjectId, patch: giftcard_batches_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_batches, giftcard_batches.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcard_variety_brands", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def giftcard_variety_brand(tree: giftcard_variety_brands,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_variety_brands",response_model= List[giftcard_variety_brands],tags = ["giftcard_variety_brands"])
async def get_giftcard_variety_brands(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_variety_brands)
    return trees

@app.get("/giftcard_variety_brands/{id}", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def get_giftcard_variety_brands_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_variety_brands, giftcard_variety_brands.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_variety_brands/{id}", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def delete_giftcard_variety_brands_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_variety_brands, giftcard_variety_brands.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_variety_brands/{id}", response_model=giftcard_variety_brands,tags = ["giftcard_variety_brands"])
async def update_giftcard_variety_brands_by_id(id: ObjectId, patch: giftcard_variety_brands_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_variety_brands, giftcard_variety_brands.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/merchant_product_order_details", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def merchant_product_order_detail(tree: merchant_product_order_details,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/merchant_product_order_details",response_model= List[merchant_product_order_details],tags = ["merchant_product_order_details"])
async def get_merchant_product_order_details(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_product_order_details)
    return trees

@app.get("/merchant_product_order_details/{id}", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def get_merchant_product_order_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_order_details, merchant_product_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_order_details/{id}", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def delete_merchant_product_order_details_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_order_details, merchant_product_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_order_details/{id}", response_model=merchant_product_order_details,tags = ["merchant_product_order_details"])
async def update_merchant_product_order_details_by_id(id: ObjectId, patch: merchant_product_order_details_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_order_details, merchant_product_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/experience_order_details", response_model=experience_order_details,tags = ["experience_order_details"])
async def experience_order_detail(tree: experience_order_details,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/experience_order_details",response_model= List[experience_order_details],tags = ["experience_order_details"])
async def get_experience_order_details(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(experience_order_details)
    return trees

@app.get("/experience_order_details/{id}", response_model=experience_order_details,tags = ["experience_order_details"])
async def get_experience_order_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_order_details, experience_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_order_details/{id}", response_model=experience_order_details,tags = ["experience_order_details"])
async def delete_experience_order_details_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_order_details, experience_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/experience_order_details/{id}", response_model=experience_order_details,tags = ["experience_order_details"])
async def update_experience_order_details_by_id(id: ObjectId, patch: experience_order_details_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_order_details, experience_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/homepage_banners", response_model=homepage_banners,tags = ["homepage_banners"])
async def homepage_banner(tree: homepage_banners,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/homepage_banners",response_model= List[homepage_banners],tags = ["homepage_banners"])
async def get_homepage_banners(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(homepage_banners)
    return trees

@app.get("/homepage_banners/{id}", response_model=homepage_banners,tags = ["homepage_banners"])
async def get_homepage_banners_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(homepage_banners, homepage_banners.id == id)
    if tree is None:
        raise HTTPException(status_code= 404)
    return tree

@app.delete("/homepage_banners/{id}", response_model=homepage_banners,tags = ["homepage_banners"])
async def delete_homepage_banners_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(homepage_banners, homepage_banners.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/homepage_banners/{id}", response_model=homepage_banners,tags = ["homepage_banners"])
async def update_homepage_banners_by_id(id: ObjectId, patch: homepage_banners_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(homepage_banners, homepage_banners.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/point_transactions", response_model=point_transactions,tags = ["point_transactions"])
async def point_transaction(tree: point_transactions,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/point_transactions",response_model= List[point_transactions],tags = ["point_transactions"])
async def get_point_transactions(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(point_transactions)
    return trees

@app.get("/point_transactions/{id}", response_model=point_transactions,tags = ["point_transactions"])
async def get_point_transactions_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(point_transactions, point_transactions.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/point_transactions/{id}", response_model=point_transactions,tags = ["point_transactions"])
async def delete_point_transactions_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(point_transactions, point_transactions.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/point_transactions/{id}", response_model=point_transactions,tags = ["point_transactions"])
async def update_point_transactions_by_id(id: ObjectId, patch: point_transactions_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(point_transactions, point_transactions.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/offer_campaign_images", response_model=offer_campaign_images,tags = ["offer_campaign_images"])
async def offer_campaign_image(tree: offer_campaign_images,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/offer_campaign_images",response_model= List[offer_campaign_images],tags = ["offer_campaign_images"])
async def get_offer_campaign_images(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(offer_campaign_images)
    return trees

@app.get("/offer_campaign_images/{id}", response_model=offer_campaign_images,tags = ["offer_campaign_images"])
async def get_offer_campaign_images_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_images, offer_campaign_images.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_images/{id}", response_model=offer_campaign_images,tags = ["offer_campaign_images"])
async def delete_offer_campaign_images_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_images, offer_campaign_images.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/offer_campaign_images/{id}", response_model=offer_campaign_images ,tags = ["offer_campaign_images"])
async def update_offer_campaign_images_by_id(id: ObjectId, patch: offer_campaign_images_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_images, offer_campaign_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

# @app.post("/user_payment_methods", response_model=user_payment_methods)
# async def user_payment_method(tree: user_payment_methods):
#     await engine.save(tree)
#     return tree

@app.post("/giftcard_units", response_model=giftcard_units,tags = ["giftcard_units"])
async def giftcard_unit(tree: giftcard_units,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_units",response_model= List[giftcard_units],tags = ["giftcard_units"])
async def get_giftcard_units(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_units)
    return trees

@app.get("/giftcard_units/{id}", response_model=giftcard_units,tags = ["giftcard_units"])
async def get_giftcard_units_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_units, giftcard_units.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_units/{id}", response_model=giftcard_units,tags = ["giftcard_units"])
async def delete_giftcard_units_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_units, giftcard_units.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_units/{id}", response_model=giftcard_units,tags = ["giftcard_units"])
async def update_giftcard_units_by_id(id: ObjectId, patch: giftcard_units_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_units, giftcard_units.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/merchant_product_categories", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def merchant_product_categorie(tree: merchant_product_categories,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/merchant_product_categories",response_model= List[merchant_product_categories],tags = ["merchant_product_categories"])
async def get_merchant_product_categories(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_product_categories)
    return trees

@app.get("/merchant_product_categories/{id}", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def get_merchant_product_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_categories, merchant_product_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_categories/{id}", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def delete_merchant_product_categories_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_categories, merchant_product_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_categories/{id}", response_model=merchant_product_categories,tags = ["merchant_product_categories"])
async def update_merchant_product_categories_by_id(id: ObjectId, patch: merchant_product_categories_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_categories, merchant_product_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/offer_campaigns", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def offer_campaign(tree: offer_campaigns,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/offer_campaigns",response_model= List[offer_campaigns],tags = ["offer_campaigns"])
async def get_offer_campaigns(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(offer_campaigns)
    return trees

@app.get("/offer_campaigns/{id}", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def get_offer_campaigns_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaigns, offer_campaigns.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaigns/{id}", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def delete_offer_campaigns_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaigns, offer_campaigns.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/offer_campaigns/{id}", response_model=offer_campaigns,tags = ["offer_campaigns"])
async def update_offer_campaigns_by_id(id: ObjectId, patch: offer_campaigns_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaigns, offer_campaigns.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/openid_providers", response_model=openid_providers,tags = ["openid_providers"])
async def openid_provider(tree: openid_providers,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/openid_providers",response_model= List[openid_providers],tags = ["openid_providers"])
async def get_openid_providers(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(openid_providers)
    return trees

@app.get("/openid_provider/{id}", response_model=openid_providers,tags = ["openid_providers"])
async def get_openid_providers_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(openid_providers, openid_providers.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/openid_providers/{id}", response_model=openid_providers,tags = ["openid_providers"])
async def delete_openid_providers_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(openid_providers, openid_providers.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/openid_providers/{id}", response_model=openid_providers,tags = ["openid_providers"])
async def update_openid_providers_by_id(id: ObjectId, patch: openid_providers_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(openid_providers, openid_providers.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

# @app.post("/administrator_access_logs", response_model=administrator_access_logs)
# async def administrator_access_log(tree: administrator_access_logs):
#     await engine.save(tree)
#     return tree

@app.post("/wallet_giftcards", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def wallet_giftcard(tree: wallet_giftcards,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/wallet_giftcards",response_model= List[wallet_giftcards],tags = ["wallet_giftcards"])
async def get_wallet_giftcards(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(wallet_giftcards)
    return trees

@app.get("/wallet_giftcards/{id}", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def get_wallet_giftcards_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(wallet_giftcards, wallet_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/wallet_giftcards/{id}", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def delete_wallet_giftcards_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(wallet_giftcards, wallet_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/wallet_giftcards/{id}", response_model=wallet_giftcards,tags = ["wallet_giftcards"])
async def update_wallet_giftcards_by_id(id: ObjectId, patch: wallet_giftcards_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(wallet_giftcards, wallet_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/delivery_methods", response_model=delivery_methods,tags = ["delivery_methods"])
async def delivery_method(tree: delivery_methods,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/delivery_methods",response_model= List[delivery_methods],tags = ["delivery_methods"])
async def get_delivery_methods(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(delivery_methods)
    return trees

@app.get("/delivery_method/{id}", response_model=delivery_methods,tags = ["delivery_methods"])
async def get_delivery_methods_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(delivery_methods, delivery_methods.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/delivery_methods/{id}", response_model=delivery_methods,tags = ["delivery_methods"])
async def delete_delivery_methods_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(delivery_methods, delivery_methods.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/delivery_methods/{id}", response_model=delivery_methods,tags = ["delivery_methods"])
async def update_delivery_methods_by_id(id: ObjectId, patch: delivery_methods_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(delivery_methods, delivery_methods.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

# @app.post("/roles", response_model=roles)
# async def role(tree: roles):
#     await engine.save(tree)
#     return tree

@app.post("/supplier_accounts", response_model=supplier_accounts,tags = ["supplier_accounts"])
async def supplier_account(tree: supplier_accounts,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/supplier_accounts",response_model= List[supplier_accounts],tags = ["supplier_accounts"])
async def get_supplier_accounts(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(supplier_accounts)
    return trees

@app.get("/supplier_accounts/{id}", response_model=supplier_accounts,tags = ["supplier_accounts"])
async def get_supplier_accounts_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(supplier_accounts, supplier_accounts.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/supplier_accounts/{id}", response_model=supplier_accounts,tags = ["supplier_accounts"])
async def delete_supplier_accounts_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(supplier_accounts, supplier_accounts.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/supplier_accounts/{id}", response_model=supplier_accounts,tags = ["supplier_accounts"])
async def update_supplier_accounts_by_id(id: ObjectId, patch: supplier_accounts_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(supplier_accounts, supplier_accounts.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/merchant_product_images", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def merchant_product_image(tree: merchant_product_images,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/merchant_product_images",response_model= List[merchant_product_images],tags = ["merchant_product_images"])
async def get_merchant_product_images(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_product_images)
    return trees

@app.get("/merchant_product_images/{id}", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def get_merchant_product_images_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_images, merchant_product_images.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_images/{id}", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def delete_merchant_product_images_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_images, merchant_product_images.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_images/{id}", response_model=merchant_product_images,tags = ["merchant_product_images"])
async def update_merchant_product_images_by_id(id: ObjectId, patch: merchant_product_images_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_images, merchant_product_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/wallets", response_model=wallets,tags = ["wallets"])
async def wallet(tree: wallets,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/wallets",response_model= List[wallets],tags = ["wallets"])
async def get_wallets(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(wallets)
    return trees

@app.get("/wallets/{id}", response_model=wallets,tags = ["wallets"])
async def get_wallets_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(wallets, wallets.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/wallets/{id}", response_model=wallets,tags = ["wallets"])
async def delete_wallets_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(wallets, wallets.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/wallets/{id}", response_model=wallets,tags = ["wallets"])
async def update_wallets_by_id(id: ObjectId, patch: wallets_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(wallets, wallets.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/whitelisted_proxies", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def whitelisted_proxie(tree: whitelisted_proxies,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/whitelisted_proxies",response_model= List[whitelisted_proxies],tags = ["whitelisted_proxies"])
async def get_whitelisted_proxies(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(whitelisted_proxies)
    return trees

@app.get("/whitelisted_proxies/{id}", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def get_whitelisted_proxies_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(whitelisted_proxies, whitelisted_proxies.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/whitelisted_proxies/{id}", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def delete_whitelisted_proxies_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(whitelisted_proxies, whitelisted_proxies.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/whitelisted_proxies/{id}", response_model=whitelisted_proxies,tags = ["whitelisted_proxies"])
async def update_whitelisted_proxies_by_id(id: ObjectId, patch: whitelisted_proxies_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(whitelisted_proxies, whitelisted_proxies.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcards", response_model=giftcards,tags = ["giftcards"])
async def giftcard(tree: giftcards,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcards",response_model= List[giftcards],tags = ["giftcards"])
async def get_giftcards(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcards)
    return trees

@app.get("/giftcard/{id}", response_model=giftcards,tags = ["giftcards"])
async def get_giftcards_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcards, giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcards/{id}", response_model=giftcards,tags = ["giftcards"])
async def delete_giftcards_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcards, giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcards/{id}", response_model=giftcards,tags = ["giftcards"])
async def update_giftcards_by_id(id: ObjectId, patch: giftcards_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcards, giftcards.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcard_terms", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def giftcard_term(tree: giftcard_terms,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_terms",response_model= List[giftcard_terms],tags = ["giftcard_terms"])
async def get_giftcard_terms(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_terms)
    return trees

@app.get("/giftcard_term/{id}", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def get_giftcard_terms_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_terms, giftcard_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_terms/{id}", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def delete_giftcard_terms_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_terms, giftcard_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_terms/{id}", response_model=giftcard_terms,tags = ["giftcard_terms"])
async def update_giftcard_terms_by_id(id: ObjectId, patch: giftcard_terms_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_terms, giftcard_terms.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/third_party_brands", response_model=third_party_brands, tags = ["third_party_brands"])
async def third_party_brand(tree: third_party_brands,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/third_party_brands",response_model= List[third_party_brands],tags = ["third_party_brands"])
async def get_third_party_brands(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(third_party_brands)
    return trees

@app.get("/third_party_brand/{id}", response_model=third_party_brands,tags = ["third_party_brands"])
async def get_third_party_brands_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(third_party_brands, third_party_brands.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/third_party_brands/{id}", response_model=third_party_brands,tags = ["third_party_brands"])
async def delete_third_party_brands_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(third_party_brands, third_party_brands.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/third_party_brands/{id}", response_model=third_party_brands,tags = ["third_party_brands"])
async def update_third_party_brands_by_id(id: ObjectId, patch: third_party_brands_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(third_party_brands, third_party_brands.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcard_types", response_model=giftcard_types, tags = ["giftcard_types"])
async def giftcard_type(tree: giftcard_types,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_types",response_model= List[giftcard_types],tags = ["giftcard_types"])
async def get_giftcard_types(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(delivery_methods)
    return trees

@app.get("/giftcard_type/{id}", response_model=giftcard_types,tags = ["giftcard_types"])
async def get_giftcard_types_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_types, giftcard_types.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_types/{id}", response_model=giftcard_types,tags = ["giftcard_types"])
async def delete_giftcard_types_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_types, giftcard_types.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_types/{id}", response_model=giftcard_types,tags = ["giftcard_types"])
async def update_giftcard_types_by_id(id: ObjectId, patch: giftcard_types_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_types, giftcard_types.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/experience_orders", response_model=experience_orders, tags = ["experience_orders"])
async def experience_order(tree: experience_orders,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/experience_orders",response_model= List[experience_orders],tags = ["experience_orders"])
async def get_experience_orders(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(experience_orders)
    return trees

@app.get("/experience_orders/{id}", response_model=experience_orders,tags = ["experience_orders"])
async def get_experience_orders_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_orders, experience_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_orders/{id}", response_model=experience_orders,tags = ["experience_orders"])
async def delete_experience_orders_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_orders, experience_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/experience_orders/{id}", response_model=experience_orders,tags = ["experience_orders"])
async def update_experience_orders_by_id(id: ObjectId, patch: experience_orders_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_orders, experience_orders.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/experience_slots", response_model=experience_slots,tags = ["experience_slots"])
async def experience_slot(tree: experience_slots,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/experience_slots",response_model= List[experience_slots],tags = ["experience_slots"])
async def get_experience_slots(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(experience_slots)
    return trees

@app.get("/experience_slots/{id}", response_model=experience_slots,tags = ["experience_slots"])
async def get_experience_slots_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db) ):
    tree = await db.engine.find_one(experience_slots, experience_slots.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_slots/{id}", response_model=experience_slots,tags = ["experience_slots"])
async def delete_experience_slots_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_slots, experience_slots.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/experience_slots/{id}", response_model=experience_slots,tags = ["experience_slots"])
async def update_experience_slots_by_id(id: ObjectId, patch: experience_slots_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_slots, experience_slots.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/suppliers", response_model=suppliers,tags = ["suppliers"])
async def supplier(tree: suppliers,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/suppliers",response_model= List[suppliers],tags = ["suppliers"])
async def get_suppliers(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(suppliers)
    return trees

@app.get("/supplier/{id}", response_model=suppliers,tags = ["suppliers"])
async def get_suppliers_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(suppliers, suppliers.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/suppliers/{id}", response_model=suppliers,tags = ["suppliers"])
async def delete_suppliers_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(suppliers, suppliers.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/suppliers/{id}", response_model=suppliers,tags = ["suppliers"])
async def update_suppliers_by_id(id: ObjectId, patch: suppliers_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(suppliers, suppliers.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/supplier_access_logs", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def supplier_access_log(tree: supplier_access_logs,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/supplier_access_logs",response_model= List[supplier_access_logs],tags = ["supplier_access_logs"])
async def get_supplier_access_logs(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(supplier_access_logs)
    return trees

@app.get("/supplier_access_log/{id}", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def get_supplier_access_logs_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(supplier_access_logs, supplier_access_logs.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/supplier_access_logs/{id}", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def delete_supplier_access_logs_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(supplier_access_logs, supplier_access_logs.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/supplier_access_logs/{id}", response_model=supplier_access_logs,tags = ["supplier_access_logs"])
async def update_supplier_access_logs_by_id(id: ObjectId, patch: supplier_access_logs_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(supplier_access_logs, supplier_access_logs.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/offer_campaign_categories", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def offer_campaign_categorie(tree: offer_campaign_categories,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/offer_campaign_categories",response_model= List[offer_campaign_categories],tags = ["offer_campaign_categories"])
async def get_offer_campaign_categories(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(offer_campaign_categories)
    return trees

@app.get("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def get_offer_campaign_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def delete_offer_campaign_categories_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def update_offer_campaign_categories_by_id(id: ObjectId, patch: offer_campaign_categories_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/experience_details", response_model=experience_details,tags = ["experience_details"])
async def experience_detail(tree: experience_details,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/experience_details",response_model= List[experience_details],tags = ["experience_details"])
async def get_experience_details(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(experience_details)
    return trees

@app.get("/experience_detail/{id}", response_model=experience_details,tags = ["experience_details"])
async def get_experience_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_details, experience_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_details/{id}", response_model=experience_details,tags = ["experience_details"])
async def delete_experience_details_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_details, experience_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/experience_details/{id}", response_model=experience_details,tags = ["experience_details"])
async def update_experience_details_by_id(id: ObjectId, patch: experience_details_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_details, experience_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/experience_order_recipients", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def experience_order_recipient(tree: experience_order_recipients,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/experience_order_recipients",response_model= List[experience_order_recipients],tags = ["experience_order_recipients"])
async def get_experience_order_recipients(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(experience_order_recipients)
    return trees

@app.get("/experience_order_recipient/{id}", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def get_experience_order_recipients_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_order_recipients, experience_order_recipients.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_order_recipients/{id}", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def delete_experience_order_recipients_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_order_recipients, experience_order_recipients.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/experience_order_recipients/{id}", response_model=experience_order_recipients,tags = ["experience_order_recipients"])
async def update_experience_order_recipients_by_id(id: ObjectId, patch: experience_order_recipients_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_order_recipients, experience_order_recipients.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcard_styles", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def giftcard_style(tree: giftcard_styles,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_styles",response_model= List[giftcard_styles],tags = ["giftcard_styles"])
async def get_giftcard_styles(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_styles)
    return trees

@app.get("/giftcard_style/{id}", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def get_giftcard_styles_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db) ):
    tree = await db.engine.find_one(giftcard_styles, giftcard_styles.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_styles/{id}", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def delete_giftcard_styles_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_styles, giftcard_styles.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_styles/{id}", response_model=giftcard_styles,tags = ["giftcard_styles"])
async def update_giftcard_styles_by_id(id: ObjectId, patch: giftcard_styles_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_styles, giftcard_styles.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/experience_images", response_model=experience_images,tags = ["experience_images"])
async def experience_image(tree: experience_images,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/experience_images",response_model= List[experience_images],tags = ["experience_images"])
async def get_experience_images(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(experience_images)
    return trees

@app.get("/experience_image/{id}", response_model=experience_images,tags = ["experience_images"])
async def get_experience_images_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_images, experience_images.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/experience_images/{id}", response_model=experience_images,tags = ["experience_images"])
async def delete_experience_images_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_styles, giftcard_styles.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/experience_images/{id}", response_model=experience_images,tags = ["experience_images"])
async def update_experience_images_by_id(id: ObjectId, patch: experience_images_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(experience_images, experience_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/variants", response_model=variants,tags = ["variants"])
async def variant(tree: variants,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/variants",response_model= List[variants],tags = ["variants"])
async def get_variants(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(variants)
    return trees

@app.get("/variant/{id}", response_model=variants,tags = ["variants"])
async def get_variants_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(variants, variants.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/variants/{id}", response_model=variants,tags = ["variants"])
async def delete_variants_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(variants, variants.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/variants/{id}", response_model=variants,tags = ["variants"])
async def update_variants_by_id(id: ObjectId, patch: variants_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(variants, variants.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcard_attributes", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def giftcard_attribute(tree: giftcard_attributes,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_attributes",response_model= List[giftcard_attributes],tags = ["giftcard_attributes"])
async def get_giftcard_attributes(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_attributes)
    return trees

@app.get("/giftcard_attribute/{id}", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def get_giftcard_attributes_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db) ):
    tree = await db.engine.find_one(giftcard_attributes, giftcard_attributes.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_attributes/{id}", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def delete_variants_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_attributes, giftcard_attributes.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_attributes/{id}", response_model=giftcard_attributes,tags = ["giftcard_attributes"])
async def update_giftcard_attributes_by_id(id: ObjectId, patch: giftcard_attributes_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_attributes, giftcard_attributes.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/user_phones", response_model=user_phones,tags = ["user_phones"])
async def user_phone(tree: user_phones,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/user_phones",response_model= List[user_phones],tags = ["user_phones"])
async def get_user_phones(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(user_phones)
    return trees

@app.get("/user_phone/{id}", response_model=user_phones,tags = ["user_phones"])
async def get_user_phones_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_phones, user_phones.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_phones/{id}", response_model=user_phones,tags = ["user_phones"])
async def delete_user_phones_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_phones, user_phones.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/user_phones/{id}", response_model=user_phones,tags = ["user_phones"])
async def update_user_phones_by_id(id: ObjectId, patch: user_phones_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_phones, user_phones.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/experience_prices", response_model=experience_prices,tags = ["offer_campaign_categories"])
async def experience_price(tree: experience_prices,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/offer_campaign_categories",response_model= List[offer_campaign_categories],tags = ["offer_campaign_categories"])
async def get_offer_campaign_categories(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(offer_campaign_categories)
    return trees

@app.get("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def get_offer_campaign_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def delete_offer_campaign_categories_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/offer_campaign_categories/{id}", response_model=offer_campaign_categories,tags = ["offer_campaign_categories"])
async def update_offer_campaign_categories_by_id(id: ObjectId, patch: offer_campaign_categories_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_categories, offer_campaign_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/brands", response_model=brands,tags = ["brands"])
async def brand(tree: brands,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/brands",response_model= List[brands],tags = ["brands"])
async def get_brands(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(brands)
    return trees

@app.get("/brands/{id}", response_model=brands,tags = ["brands"])
async def get_brands_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brands, brands.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/brands/{id}", response_model=brands,tags = ["brands"])
async def delete_brands_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brands, brands.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/brands/{id}", response_model=brands,tags = ["brands"])
async def update_brands_by_id(id: ObjectId, patch: brands_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(brands, brands.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/offer_campaign_terms", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def offer_campaign_term(tree: offer_campaign_terms,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/offer_campaign_terms",response_model= List[offer_campaign_terms],tags = ["offer_campaign_terms"])
async def get_offer_campaign_terms(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(offer_campaign_terms)
    return trees

@app.get("/offer_campaign_terms/{id}", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def get_offer_campaign_terms_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_terms, offer_campaign_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_terms/{id}", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def delete_offer_campaign_terms_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_terms, offer_campaign_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/offer_campaign_terms/{id}", response_model=offer_campaign_terms,tags = ["offer_campaign_terms"])
async def update_offer_campaign_terms_by_id(id: ObjectId, patch: offer_campaign_terms_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_terms, offer_campaign_terms.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/interface_methods", response_model=interface_methods,tags = ["interface_methods"])
async def interface_method(tree: interface_methods,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/interface_methods",response_model= List[interface_methods],tags = ["interface_methods"])
async def get_offer_campaign_categories(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(interface_methods)
    return trees

@app.get("/interface_methods/{id}", response_model=interface_methods,tags = ["interface_methods"])
async def get_interface_methods_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(interface_methods, interface_methods.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/interface_methods/{id}", response_model=interface_methods,tags = ["interface_methods"])
async def delete_interface_methods_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(interface_methods, interface_methods.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/interface_methods/{id}", response_model=interface_methods,tags = ["interface_methods"])
async def update_interface_methods_by_id(id: ObjectId, patch: interface_methods_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(interface_methods, interface_methods.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/merchant_product_transaction_categories", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def merchant_product_transaction_categorie(tree: merchant_product_transaction_categories,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/merchant_product_transaction_categories",response_model= List[merchant_product_transaction_categories],tags = ["merchant_product_transaction_categories"])
async def get_merchant_product_transaction_categories(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_product_transaction_categories)
    return trees

@app.get("/merchant_product_transaction_categories/{id}", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def get_merchant_product_transaction_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_transaction_categories, merchant_product_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree


@app.delete("/merchant_product_transaction_categories/{id}", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def delete_merchant_product_transaction_categories_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_transaction_categories, merchant_product_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_transaction_categories/{id}", response_model=merchant_product_transaction_categories,tags = ["merchant_product_transaction_categories"])
async def update_merchant_product_transaction_categories_by_id(id: ObjectId, patch: merchant_product_transaction_categories_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_transaction_categories, merchant_product_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcard_denominations", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def giftcard_denomination(tree: giftcard_denominations,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_denominations",response_model= List[giftcard_denominations],tags = ["giftcard_denominations"])
async def get_giftcard_denominations(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_denominations)
    return trees

@app.get("/giftcard_denominations/{id}", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def get_offer_campaign_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_denominations, giftcard_denominations.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_denominations/{id}", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def delete_giftcard_denominations_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_denominations, giftcard_denominations.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_denominations/{id}", response_model=giftcard_denominations,tags = ["giftcard_denominations"])
async def update_giftcard_denominations_by_id(id: ObjectId, patch: giftcard_denominations_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_denominations, giftcard_denominations.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/gifts", response_model=gifts,tags = ["gifts"])
async def gift(tree: gifts,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/gifts",response_model= List[gifts],tags = ["gifts"])
async def get_gifts(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(gifts)
    return trees

@app.get("/gift/{id}", response_model=gifts,tags = ["gifts"])
async def get_gifts_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(gifts, gifts.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/gifts/{id}", response_model=gifts,tags = ["gifts"])
async def delete_gifts_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(gifts, gifts.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/gifts/{id}", response_model=gifts,tags = ["gifts"])
async def update_gifts_by_id(id: ObjectId, patch: gifts_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(gifts, gifts.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/merchant_product_variants", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def merchant_product_variant(tree: merchant_product_variants,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/merchant_product_variants",response_model= List[merchant_product_variants],tags = ["merchant_product_variants"])
async def get_merchant_product_variants(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_product_variants)
    return trees

@app.get("/merchant_product_variants/{id}", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def get_merchant_product_variants_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_variants, merchant_product_variants.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_variants/{id}", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def delete_merchant_product_variants_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_variants, merchant_product_variants.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_variants/{id}", response_model=merchant_product_variants,tags = ["merchant_product_variants"])
async def update_merchant_product_variants_by_id(id: ObjectId, patch: merchant_product_variants_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_variants, merchant_product_variants.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/user_order_details_giftcards", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def user_order_details_giftcard(tree: user_order_details_giftcards,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/user_order_details_giftcards",response_model= List[user_order_details_giftcards],tags = ["user_order_details_giftcards"])
async def get_user_order_details_giftcards(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(user_order_details_giftcards)
    return trees

@app.get("/user_order_details_giftcards/{id}", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def get_user_order_details_giftcards_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_order_details_giftcards, user_order_details_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_order_details_giftcards/{id}", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def delete_user_order_details_giftcards_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_order_details_giftcards, user_order_details_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/user_order_details_giftcards/{id}", response_model=user_order_details_giftcards,tags = ["user_order_details_giftcards"])
async def update_user_order_details_giftcards_by_id(id: ObjectId, patch: user_order_details_giftcards_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_order_details_giftcards, user_order_details_giftcards.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/user_addresses", response_model=user_addresses,tags = ["user_addresses"])
async def user_addresse(tree: user_addresses,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/user_addresses",response_model= List[user_addresses],tags = ["user_addresses"])
async def get_user_addresses(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(user_addresses)
    return trees

@app.get("/user_addresses/{id}", response_model=user_addresses,tags = ["user_addresses"])
async def get_user_addresses_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_addresses, user_addresses.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_addresses/{id}", response_model=user_addresses,tags = ["user_addresses"])
async def delete_user_addresses_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_addresses, user_addresses.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/user_addresses/{id}", response_model=user_addresses,tags = ["user_addresses"])
async def update_user_addresses_by_id(id: ObjectId, patch: user_addresses_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_addresses, user_addresses.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

# @app.post("/user_credit_cards", response_model=user_credit_cards)
# async def user_credit_card(tree: user_credit_cards):
#     await engine.save(tree)
#     return tree

@app.post("/countries", response_model=countries,tags = ["countries"])
async def create_tree(tree: countries,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/countries",response_model= List[countries],tags = ["countries"])
async def get_countries(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(countries)
    return trees

@app.get("/countries/{id}", response_model=countries,tags = ["countries"])
async def get_countries_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(countries, countries.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/countries/{id}", response_model=countries,tags = ["countries"])
async def delete_countries_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(countries, countries.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/countries/{id}", response_model=countries,tags = ["countries"])
async def update_countries_by_id(id: ObjectId, patch: countries_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(countries, countries.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/categories", response_model=categories,tags = ["categories"])
async def categorie(tree: categories,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/categories",response_model= List[categories],tags = ["categories"])
async def get_categories(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(categories)
    return trees

@app.get("/offer_campaign_categories/{id}", response_model=categories,tags = ["categories"])
async def get_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(categories, categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/categories/{id}", response_model=categories,tags = ["categories"])
async def delete_categories_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(categories, categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/categories/{id}", response_model=categories,tags = ["categories"])
async def update_categories_by_id(id: ObjectId, patch: categories_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(categories, categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/redemption_partners", response_model=redemption_partners,tags = ["redemption_partners"])
async def redemption_partner(tree: redemption_partners,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/redemption_partners",response_model= List[redemption_partners],tags = ["redemption_partners"])
async def get_redemption_partners(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(redemption_partners)
    return trees

@app.get("/redemption_partners/{id}", response_model=redemption_partners,tags = ["redemption_partners"])
async def get_redemption_partners_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(redemption_partners, redemption_partners.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree


@app.delete("/redemption_partners/{id}", response_model=redemption_partners,tags = ["redemption_partners"])
async def delete_redemption_partners_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(redemption_partners, redemption_partners.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/redemption_partners/{id}", response_model=redemption_partners,tags = ["redemption_partners"])
async def update_redemption_partners_by_id(id: ObjectId, patch: redemption_partners_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(redemption_partners, redemption_partners.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/user_openids", response_model=user_openids,tags = ["user_openids"])
async def user_openid(tree: user_openids,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/user_openids",response_model= List[user_openids],tags = ["user_openids"])
async def get_user_openids(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(user_openids)
    return trees

@app.get("/user_openids/{id}", response_model=user_openids,tags = ["user_openids"])
async def get_user_openids_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_openids, user_openids.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_openids/{id}", response_model=user_openids,tags = ["user_openids"])
async def delete_user_openids_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_openids, user_openids.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/user_openids/{id}", response_model=user_openids,tags = ["user_openids"])
async def update_user_openids_by_id(id: ObjectId, patch: user_openids_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_openids, user_openids.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/transaction_categories", response_model=transaction_categories,tags = ["transaction_categories"])
async def transaction_categorie(tree: transaction_categories,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/transaction_categories",response_model= List[transaction_categories],tags = ["transaction_categories"])
async def get_transaction_categories(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(transaction_categories)
    return trees

@app.get("/transaction_categories/{id}", response_model=transaction_categories,tags = ["transaction_categories"])
async def get_transaction_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(transaction_categories, transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/transaction_categories/{id}", response_model=transaction_categories,tags = ["transaction_categories"])
async def delete_transaction_categories_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(transaction_categories, transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/transaction_categories/{id}", response_model=transaction_categories,tags = ["transaction_categories"])
async def update_transaction_categories_by_id(id: ObjectId, patch: transaction_categories_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(transaction_categories, transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/giftcard_batch_giftcard_details", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def giftcard_batch_giftcard_detail(tree: giftcard_batch_giftcard_details,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_batch_giftcard_details",response_model= List[giftcard_batch_giftcard_details],tags = ["giftcard_batch_giftcard_details"])
async def get_giftcard_batch_giftcard_details(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_batch_giftcard_details)
    return trees

@app.get("/giftcard_batch_giftcard_details/{id}", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def get_giftcard_batch_giftcard_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_batch_giftcard_details, giftcard_batch_giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_batch_giftcard_details/{id}", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def delete_giftcard_batch_giftcard_details_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_batch_giftcard_details, giftcard_batch_giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_batch_giftcard_details/{id}", response_model=giftcard_batch_giftcard_details,tags = ["giftcard_batch_giftcard_details"])
async def update_giftcard_batch_giftcard_details_by_id(id: ObjectId, patch: giftcard_batch_giftcard_details_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_batch_giftcard_details, giftcard_batch_giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/giftcard_variety_denominations", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def giftcard_variety_denomination(tree: giftcard_variety_denominations,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_variety_denominations",response_model= List[giftcard_variety_denominations],tags = ["giftcard_variety_denominations"])
async def get_giftcard_variety_denominations(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_variety_denominations)
    return trees

@app.get("/giftcard_variety_denominations/{id}", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def get_giftcard_variety_denominations_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_variety_denominations, giftcard_variety_denominations.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_variety_denominations/{id}", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def delete_giftcard_variety_denominations_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_variety_denominations, giftcard_variety_denominations.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_variety_denominations/{id}", response_model=giftcard_variety_denominations,tags = ["giftcard_variety_denominations"])
async def update_giftcard_variety_denominations_by_id(id: ObjectId, patch: giftcard_variety_denominations_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_variety_denominations, giftcard_variety_denominations.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/users", response_model=users,tags = ["users"])
async def create_users(tree: users,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/users",response_model= List[users],tags = ["users"])
async def get_users(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(users)
    return trees

@app.get("/user/{id}", response_model=users,tags = ["users"])
async def get_users_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(users, users.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/users/{id}", response_model=users,tags = ["users"])
async def delete_users_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(users, users.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/users/{id}", response_model=users,tags = ["users"])
async def update_users_by_id(id: ObjectId, patch: users_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(users, users.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/giftcard_details", response_model=giftcard_details,tags = ["giftcard_details"])
async def giftcard_detail(tree: giftcard_details,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_details",response_model= List[giftcard_details],tags = ["giftcard_details"])
async def get_giftcard_details(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_details)
    return trees

@app.get("/giftcard_detail/{id}", response_model=giftcard_details,tags = ["giftcard_details"])
async def get_giftcard_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_details, giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_details/{id}", response_model=giftcard_details,tags = ["giftcard_details"])
async def delete_users_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_details, giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_details/{id}", response_model=giftcard_details,tags = ["giftcard_details"])
async def update_giftcard_details_by_id(id: ObjectId, patch: giftcard_details_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_details, giftcard_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/third_party_order_details", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def third_party_order_detail(tree: third_party_order_details,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/third_party_order_details",response_model= List[third_party_order_details],tags = ["third_party_order_details"])
async def get_third_party_order_details(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(third_party_order_details)
    return trees

@app.get("/third_party_order_details/{id}", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def get_third_party_order_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(third_party_order_details, third_party_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/third_party_order_details/{id}", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def delete_users_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(third_party_order_details, third_party_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/third_party_order_details/{id}", response_model=third_party_order_details,tags = ["third_party_order_details"])
async def update_third_party_order_details_by_id(id: ObjectId, patch: third_party_order_details_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(third_party_order_details, third_party_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/user_orders", response_model=user_orders,tags = ["user_orders"])
async def user_order(tree: user_orders,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/user_orders",response_model= List[user_orders],tags = ["user_orders"])
async def get_user_orders(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(user_orders)
    return trees

@app.get("/user_orders/{id}", response_model=user_orders,tags = ["user_orders"])
async def get_user_orders_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_orders, user_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_orders/{id}", response_model=user_orders,tags = ["user_orders"])
async def delete_user_orders_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_orders, user_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/user_orders/{id}", response_model=user_orders,tags = ["user_orders"])
async def update_user_orders_by_id(id: ObjectId, patch: user_orders_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_orders, user_orders.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/offer_order_details", response_model=offer_order_details,tags = ["offer_order_details"])
async def offer_order_detail(tree: offer_order_details,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/offer_order_details",response_model= List[offer_order_details],tags = ["offer_order_details"])
async def get_offer_order_details(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(offer_order_details)
    return trees

@app.get("/offer_order_details/{id}", response_model=offer_order_details,tags = ["offer_order_details"])
async def get_offer_order_details_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_order_details, offer_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_order_details/{id}", response_model=offer_order_details,tags = ["offer_order_details"])
async def delete_offer_order_details_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_order_details, offer_order_details.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/offer_order_details/{id}", response_model=offer_order_details,tags = ["offer_order_details"])
async def update_offer_order_details_by_id(id: ObjectId, patch: offer_order_details_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_order_details, offer_order_details.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/giftcard_style_images", response_model=giftcard_style_images,tags = ["giftcard_style_images"])
async def giftcard_style_image(tree: giftcard_style_images,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_style_images",response_model= List[giftcard_style_images],tags = ["giftcard_style_images"])
async def get_giftcard_style_images(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_style_images)
    return trees

@app.get("/giftcard_style_images/{id}", response_model=giftcard_style_images,tags = ["giftcard_style_images"])
async def get_giftcard_style_images_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_style_images, giftcard_style_images.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_style_images/{id}", response_model=giftcard_style_images,tags = ["giftcard_style_images"])
async def delete_giftcard_style_images_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_style_images, giftcard_style_images.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_style_images/{id}", response_model=giftcard_style_images, tags = ["giftcard_style_images"])
async def update_giftcard_style_images_by_id(id: ObjectId, patch: giftcard_style_images_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_style_images, giftcard_style_images.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/merchant_product_terms", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def merchant_product_term(tree: merchant_product_terms,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/merchant_product_terms",response_model= List[merchant_product_terms],tags = ["merchant_product_terms"])
async def get_merchant_product_terms(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_product_terms)
    return trees

@app.get("/merchant_product_terms/{id}", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def get_merchant_product_terms_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_terms, merchant_product_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_product_terms/{id}", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def delete_giftcard_style_images_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_terms, merchant_product_terms.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_product_terms/{id}", response_model=merchant_product_terms,tags = ["merchant_product_terms"])
async def update_merchant_product_terms_by_id(id: ObjectId, patch: merchant_product_terms_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_product_terms, merchant_product_terms.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/merchant_products", response_model=merchant_products,tags = ["merchant_products"])
async def merchant_product(tree: merchant_products,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree


@app.get("/merchant_products",response_model= List[merchant_products],tags = ["merchant_products"])
async def get_merchant_products(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(merchant_products)
    return trees

@app.get("/merchant_products/{id}", response_model=merchant_products,tags = ["merchant_products"])
async def get_merchant_products_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_products, merchant_products.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/merchant_products/{id}", response_model=merchant_products,tags = ["merchant_products"])
async def delete_merchant_products_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_products, merchant_products.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/merchant_products/{id}", response_model=merchant_products ,tags = ["merchant_products"])
async def update_merchant_products_by_id(id: ObjectId, patch: merchant_products_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(merchant_products, merchant_products.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/variant_values", response_model=variant_values,tags = ["variant_values"])
async def variant_value(tree: variant_values,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/variant_values",response_model= List[variant_values],tags = ["variant_values"])
async def get_variant_values(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(variant_values)
    return trees

@app.get("/variant_values/{id}", response_model=variant_values,tags = ["variant_values"])
async def get_variant_values_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(variant_values, variant_values.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/variant_values/{id}", response_model=variant_values,tags = ["variant_values"])
async def delete_variant_values_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(variant_values, variant_values.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/variant_values/{id}", response_model=variant_values, tags = ["variant_values"])
async def update_variant_values_by_id(id: ObjectId, patch: variant_values_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(variant_values, variant_values.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/offer_orders", response_model=offer_orders,tags = ["offer_orders"])
async def offer_order(tree: offer_orders,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/offer_orders",response_model= List[offer_orders],tags = ["offer_orders"])
async def get_offer_orders(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(offer_orders)
    return trees

@app.get("/offer_orders/{id}", response_model=offer_orders,tags = ["offer_orders"])
async def get_offer_orders_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_orders, offer_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_orders/{id}", response_model=offer_orders,tags = ["offer_orders"])
async def delete_offer_orders_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_orders, offer_orders.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/offer_orders/{id}", response_model=offer_orders, tags = ["offer_orders"])
async def update_offer_orders_by_id(id: ObjectId, patch: offer_orders_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_orders, offer_orders.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree


@app.post("/giftcard_varieties", response_model=giftcard_varieties,tags = ["giftcard_varieties"])
async def giftcard_varietie(tree: giftcard_varieties,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/giftcard_varieties",response_model= List[giftcard_varieties],tags = ["giftcard_varieties"])
async def get_giftcard_varieties(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(giftcard_varieties)
    return trees

@app.get("/giftcard_varieties/{id}", response_model=giftcard_varieties,tags = ["giftcard_varieties"])
async def get_giftcard_varieties_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db) ):
    tree = await db.engine.find_one(giftcard_varieties, giftcard_varieties.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/giftcard_varieties/{id}", response_model=giftcard_varieties,tags = ["giftcard_varieties"])
async def delete_giftcard_varieties_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_varieties, giftcard_varieties.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/giftcard_varieties/{id}", response_model=giftcard_varieties, tags= ["giftcard_varieties"])
async def update_giftcard_varieties_by_id(id: ObjectId, patch: giftcard_varieties_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(giftcard_varieties, giftcard_varieties.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/schema_migrations", response_model=schema_migrations,tags = ["schema_migrations"])
async def schema_migration(tree: schema_migrations,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/schema_migrations",response_model= List[schema_migrations],tags = ["schema_migrations"])
async def get_schema_migrations(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(schema_migrations)
    return trees

@app.get("/schema_migration/{id}", response_model=schema_migrations,tags = ["schema_migrations"])
async def get_schema_migrations_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(schema_migrations, schema_migrations.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/schema_migrations/{id}", response_model=schema_migrations,tags = ["schema_migrations"])
async def delete_schema_migrations_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(schema_migrations, schema_migrations.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/schema_migrations/{id}", response_model=schema_migrations, tags= ["schema_migrations"])
async def update_schema_migrations_by_id(id: ObjectId, patch: schema_migrations_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(schema_migrations, schema_migrations.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/offer_campaign_transaction_categories", response_model=offer_campaign_transaction_categories ,tags = ["offer_campaign_transaction_categories"])
async def offer_campaign_transaction_categorie(tree: offer_campaign_transaction_categories,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/offer_campaign_transaction_categories",response_model= List[offer_campaign_transaction_categories],tags = ["offer_campaign_transaction_categories"])
async def get_offer_campaign_transaction_categories(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(offer_campaign_transaction_categories)
    return trees

@app.get("/offer_campaign_transaction_category/{id}", response_model=offer_campaign_transaction_categories,tags = ["offer_campaign_transaction_categories"])
async def get_offer_campaign_transaction_categories_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_transaction_categories, offer_campaign_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/offer_campaign_transaction_categories/{id}", response_model=offer_campaign_transaction_categories,tags = ["offer_campaign_transaction_categories"])
async def delete_offer_campaign_transaction_categories_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_transaction_categories, offer_campaign_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/offer_campaign_transaction_categories/{id}", response_model=offer_campaign_transaction_categories, tags= ["offer_campaign_transaction_categories"])
async def update_offer_campaign_transaction_categories_by_id(id: ObjectId, patch: offer_campaign_transaction_categories_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(offer_campaign_transaction_categories, offer_campaign_transaction_categories.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/normalized_addresses", response_model=normalized_addresses,tags = ["normalized_addresses"])
async def normalized_addresse(tree: normalized_addresses,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/normalized_addresses",response_model= List[normalized_addresses],tags = ["normalized_addresses"])
async def get_normalized_addresses(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(normalized_addresses)
    return trees

@app.get("/offer_campaign_transaction_categories/{id}", response_model=normalized_addresses,tags = ["normalized_addresses"])
async def get_normalized_addresses_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(normalized_addresses, normalized_addresses.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/normalized_addresses/{id}", response_model=normalized_addresses,tags = ["normalized_addresses"])
async def delete_normalized_addresses_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(normalized_addresses, normalized_addresses.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/normalized_addresses/{id}", response_model=normalized_addresses, tags= ["normalized_addresses"])
async def update_normalized_addresses_by_id(id: ObjectId, patch: normalized_addresses_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(normalized_addresses, normalized_addresses.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
    return tree

@app.post("/user_emails", response_model=user_emails,tags = ["user_emails"])
async def user_email(tree: user_emails,db: AsyncIOMotorClient = Depends(Db)):
    await db.engine.save(tree)
    return tree

@app.get("/user_emails",response_model= List[user_emails],tags = ["user_emails"])
async def get_user_emails(db: AsyncIOMotorClient = Depends(Db)):
    trees = await db.engine.find(user_emails)
    return trees

@app.get("/user_emails/{id}", response_model=user_emails,tags = ["user_emails"])
async def get_user_emails_by_id(id: ObjectId, db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_emails, user_emails.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_emails/{id}", response_model=user_emails,tags = ["user_emails"])
async def delete_user_emails_by_id(id: ObjectId,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_emails, user_emails.id == id)
    if tree is None:
        raise HTTPException(404)
    await db.engine.delete(tree)
    return tree

@app.patch("/user_emails/{id}", response_model=user_emails, tags= ["user_emails"])
async def update_user_emails_by_id(id: ObjectId, patch: user_emails_update,db: AsyncIOMotorClient = Depends(Db)):
    tree = await db.engine.find_one(user_emails, user_emails.id == id)
    if tree is None:
        raise HTTPException(404)

    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await db.engine.save(tree)
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

