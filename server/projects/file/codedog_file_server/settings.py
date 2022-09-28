#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021-2022 THL A29 Limited
#
# This source code file is made available under MIT License
# See LICENSE for details
# ==============================================================================
"""
Django settings for codedog_file_server project.

Generated by "django-admin startproject" using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import sys
from pathlib import Path

import pymysql
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / "subdir".
PROJECT_PATH = Path(__file__).resolve(strict=True).parent.parent

sys.path.insert(0, os.path.join(PROJECT_PATH, "utils"))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "@z1!4&x+6f&gu#9#e(y4_m@c2r(3*8l0^s9aie24pe^a*xx8*("

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "apps.base",
    "apps.authenmgr",
    "apps.filemgr",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "codedog_file_server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "codedog_file_server.wsgi.application"

FILE_UPLOAD_HANDLERS = ["django.core.files.uploadhandler.TemporaryFileUploadHandler"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": PROJECT_PATH / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "zh-Hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

# 静态文件本地路径
STATIC_ROOT = os.path.join(PROJECT_PATH, "static")

AUTH_USER_MODEL = "authenmgr.UserProfile"

SESSION_COOKIE_NAME = "codedog_file_sessionid"

# 日志
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "-%(asctime)s-%(levelname)s-%(name)s: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": os.path.join(PROJECT_PATH, "log", "codedog_file.log"),
            "maxBytes": 1 << 28,
            "backupCount": 5
        },

        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": os.path.join(PROJECT_PATH, "log", "codedog_error_file.log"),
            "maxBytes": 1 << 28,
            "backupCount": 5
        },
    },
    "loggers": {
        "": {
            "handlers": [
                "file",
                "error",
                "console"
            ],
            "level": "DEBUG",
            "propagate": True,
        },
    }
}

# ==============================================
# DRF接口设置
# ==============================================
REST_FRAMEWORK = {
    # Use Django"s standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "codedog_file_server.authentication.MainServerInternalAuthentication",
        "codedog_file_server.authentication.MainProxyAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "EXCEPTION_HANDLER": "utils.handler.custom_exception_handler"
}

# ==============================================
# 存储设置
# ==============================================
# 本地存储
STORAGE = {
    "CLIENT": os.environ.get("FILE_STORAGE_CLIENT", "utils.file_storage.LocalFilesystemStorageClient"),  # 存储方式
    "OPTIONS": {
        # 本地存储根目录
        "DEFAULT_STORAGE_ROOT_DIR": os.environ.get("FILE_STORAGE_DIR", "data/"),
    }
}

# ==============================================
# Celery 配置地址
# ==============================================

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_PASSWD = os.environ.get("REDIS_PASSWD")
REDIS_DBID = os.environ.get("REDIS_DBID")
if REDIS_PASSWD:
    CELERY_BROKER_URL = "redis://:%s@%s:%s/%s" % (REDIS_PASSWD, REDIS_HOST, REDIS_PORT, REDIS_DBID)
else:
    CELERY_BROKER_URL = "redis://%s:%s/%s" % (REDIS_HOST, REDIS_PORT, REDIS_DBID)

# ==============================================
# Sentry 数据上报地址
# ==============================================
SENTRY_DSN = os.environ.get("SENTRY_DSN")

if not DEBUG:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        send_default_pii=True
    )

# ==============================================
# 加载本地local.py
# ==============================================
try:
    sys.path.insert(0, os.path.join(PROJECT_PATH, "codedog_file_server", "env"))
    from local import *
except ImportError:
    pass