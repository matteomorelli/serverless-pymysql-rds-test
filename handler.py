
# Copyleft 2018 Matteo Morelli <matteo.morelli@gmail.com>
# SPDX-License-Identifier: AGPL-3.0-only

import os
import logging
import pymysql.cursors
import json


def rds_version(event, context):
    rds_host = os.environ['mysqlEndpoint']
    rds_port = os.environ['mysqlPort']
    name = os.environ['mysqlUser']
    password = os.environ['mysqlPassword']
    db_name = os.environ['mysqlDatabase']
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Build connection and execute connection to DB
    try:
        connection = pymysql.connect(host=rds_host,
                                     port=rds_port,
                                     user=name,
                                     password=password,
                                     db=db_name,
                                     connect_timeout=15,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        logger.info("SUCCESS: connection to RDS mysql instance succeeded")
    except pymysql.err.OperationalError as exc:
        response = {
            "statusCode": 500,
            "body": json.dumps({"msg": exc})
        }
        logger.error("ERROR: connection to RDS mysql instance succeeded")
        return response

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "SELECT VERSION()"
            cursor.execute(sql)
            result = cursor.fetchone()
            response = {
                "statusCode": 200,
                "body": json.dumps({"msg": result})
            }
            logger.info("SUCCESS: query execution completed")
    except pymysql.err.OperationalError as exc:
            logger.error("ERROR: Could not execute query on RDS instance.")
            response = {
                "statusCode": 500,
                "body": json.dumps({"msg": exc})
            }
    return response

def rds_connect(event, context):
    rds_host = os.environ['mysqlEndpoint']
    rds_port = os.environ['mysqlPort']
    name = os.environ['mysqlUser']
    password = os.environ['mysqlPassword']
    db_name = os.environ['mysqlDatabase']
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Build connection and execute connection to DB
    try:
        connection = pymysql.connect(host=rds_host,
                                     port=rds_port,
                                     user=name,
                                     password=password,
                                     db=db_name,
                                     connect_timeout=15,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        logger.info("SUCCESS: connection to RDS mysql instance succeeded")
    except pymysql.err.OperationalError as exc:
        response = {
            "statusCode": 500,
            "body": json.dumps({"msg": exc})
        }
        logger.error("ERROR: connection to RDS mysql instance succeeded")
        return response

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            response = {
                "statusCode": 200,
                "body": json.dumps({"msg": result})
            }
            logger.info("SUCCESS: query execution completed")
    except pymysql.err.OperationalError as exc:
            logger.error("ERROR: Could not execute query on RDS instance.")
            response = {
                "statusCode": 500,
                "body": json.dumps({"msg": exc})
            }
    return response
