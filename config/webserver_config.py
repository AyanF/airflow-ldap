#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Default configuration for the Airflow webserver"""
import os


from flask_appbuilder.security.manager import AUTH_LDAP

AUTH_TYPE = AUTH_LDAP
AUTH_LDAP_SERVER = "ldap://openldap:389"
AUTH_LDAP_USE_TLS = False

AUTH_LDAP_SEARCH = "dc=netflux,dc=com"
AUTH_LDAP_UID_FIELD = "cn"


AUTH_LDAP_BIND_USER = "cn=admin,dc=netflux,dc=com"
AUTH_LDAP_BIND_PASSWORD = "admin"

AUTH_USER_REGISTRATION = True  
AUTH_USER_REGISTRATION_ROLE = "Public" 
AUTH_LDAP_FIRSTNAME_FIELD = "givenName"
AUTH_LDAP_LASTNAME_FIELD = "sn"
AUTH_LDAP_EMAIL_FIELD = "mail"

AUTH_ROLES_MAPPING = {
    "cn=Marketing,ou=Groups,dc=netflux,dc=com": ["marketing"],
    "cn=Data_science,ou=Groups,dc=netflux,dc=com": ["data_science"],
    "cn=Admin,ou=Groups,dc=netflux,dc=com": ["Admin"],
}

AUTH_LDAP_GROUP_FIELD = "memberOf"

AUTH_ROLES_SYNC_AT_LOGIN = True

PERMANENT_SESSION_LIFETIME = 1800

