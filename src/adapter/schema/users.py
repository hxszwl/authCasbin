#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   wush
@License :   (C) Copyright 2021-9999, {AKULAKU}
@Contact :   
@Software:   PyCharm
@File    :   users.py
@Time    :   2023/3/23 20:08
@Desc    :

'''

__author__ = "wush"

from typing import Optional, List

from pydantic import BaseModel, Field, BaseSettings

from adapter.schema.baseResponse import ResponseModel
from infrastructure.config.config import system_config


class AppTokenConfig(BaseSettings):
    """
    在终端通过以下命令生成一个新的密匙:
    openssl rand -hex 32
    加密密钥 这个很重要千万不能泄露了，而且一定自己生成并替换。
    """
    SECRET_KEY: str = system_config.secret_key
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # token失效时间


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = Field(default=None)
    scopes: List[str] = []


class User(BaseModel):
    username: str = Field(...)
    email: Optional[str] = Field(default=None)
    full_name: Optional[str] = Field(default=None)
    is_active: bool = Field(default=False)  # 是否激活


class UserInDB(User):
    hashed_password: str = Field(...)


class UserListInputDto(BaseModel):
    pass


class UserListOutputData(BaseModel):
    """
        todo: 展示用户的关键字段信息
    """
    pass


class UserListOutputDto(ResponseModel):
    data: Optional[List[UserListOutputData]]


if __name__ == '__main__':
    pass
