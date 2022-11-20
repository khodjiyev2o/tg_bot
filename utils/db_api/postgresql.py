from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DATABASE_USER,
            password=config.DATABASE_PASSWORD,
            host=config.DATABASE_HOST,
            database=config.DATABASE_NAME,
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    # async def create_table_users(self):
    #     sql = """
    #     CREATE TABLE IF NOT EXISTS service_user (
    #     id SERIAL PRIMARY KEY,
    #     full_name VARCHAR(255) NOT NULL,
    #     username varchar(255) NULL,
    #     telegram_id BIGINT NOT NULL UNIQUE 
    #     );
    #     """
    #     await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO service_user (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM service_user"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM service_user WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM service_user"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE service_user SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM service_user WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE service_user", execute=True)

   ## Ish beruvchilar uchun

    async def get_employers(self):
        sql = "SELECT * FROM service_employer"
        return await self.execute(sql, fetch=True)

    async def get_companies_by_employer(self, employer_id):
        sql = f"""SELECT * FROM service_company WHERE service_company.employer_name_id='{employer_id}' """
        return await self.execute(sql, fetch=True)

    async def count_employers(self):
        sql = "SELECT COUNT(*) FROM service_employer"
        return await self.execute(sql, fetchval=True)

    async def get_all_companies(self):
        sql = f"SELECT * FROM service_company'"
        return await self.execute(sql, fetch=True)

    async def count_companies_by_employer(self,employer_id):
        sql = f"SELECT COUNT(*) FROM service_company WHERE service_company.employer_name_id='{employer_id}'"
        return await self.execute(sql, fetchval=True)

    async def drop_employer(self):
        await self.execute("DROP TABLE service_employer", execute=True)





    ##  Applicant uchun 
    # user_id 
    # company
    # employer
    async def create_applicant(self,user_id,company,employer):
        sql = "INSERT INTO service_applicant (user_id, company, employer) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, user_id, company, employer, fetchrow=True)

    async def get_all_applicants_by_employer(self,employer_id):
        sql = f"SELECT COUNT(*) FROM service_applicant WHERE service_applicant.employer_id='{employer_id}'"
        return await self.execute(sql, fetchval=True)

        