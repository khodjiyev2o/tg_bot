
import asyncio

from utils.db_api.postgresql import Database


async def test():
    
    db = Database()
    #await db.drop_users()
    await db.create()

    print("Users jadvalini yaratamiz...")
    
    await db.create_table_users()
    print("Yaratildi")

    users = await db.select_all_users()
    if users:
        print("Foydalanuvchilarni uchiramiz")
        await db.delete_users()
    
    print("Foydalanuvchilarni qo'shamiz")
    await db.add_user("anvar", "sariqdev", 123456789)
    await db.add_user("olim", "olim223", 12341123)
    await db.add_user("1", "1", 131231)
    await db.add_user("1", "1", 23324234)
    await db.add_user("John", "JohnDoe", 4388229)
    print("Qo'shildi")


    users = await db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=5)
    print(f"Foydalanuvchi: {user}")


## Run it when you need to test the bot
## asyncio.run(test())