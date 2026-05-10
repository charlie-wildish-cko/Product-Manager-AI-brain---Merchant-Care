{
  "openapi": "3.0.1",
  "info": {
    "title": "User Management API v1",
    "description": "An API for team and user management",
    "contact": {
      "name": "IAM Team",
      "email": "access-team@checkout.com"
    },
    "version": "1"
  },
  "paths": {
    "/api/internal/users/{userId}/activate": {
      "post": {
        "tags": [
          "ActivateUser"
        ],
        "summary": "Generate new activation url.",
        "operationId": "catActivateUser",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "New url",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.ActivateUserResponse"
                }
              }
            }
          },
          "400": {
            "description": "If user id is malformed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the the user doesn't exist.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "409": {
            "description": "If the the user state in Okta is not Staged or Provisioned."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/okta-event-hook": {
      "get": {
        "tags": [
          "AuditLogHook",
          "PublicEndpoint"
        ],
        "summary": "https://developer.okta.com/docs/concepts/event-hooks/#one-time-verification-request",
        "operationId": "oktaGetEventHook",
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      },
      "post": {
        "tags": [
          "AuditLogHook",
          "PublicEndpoint"
        ],
        "summary": "To debug this endpoint locally:\r\n1- From CLI, run ngrok with: $> ngrok http -subdomain checkout-okta -region eu 5000\r\n2- Run API locally",
        "operationId": "oktaPostEventHook",
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/cat/clients/{clientId}/providers": {
      "post": {
        "tags": [
          "ClientProviders"
        ],
        "operationId": "saveClientProviders",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.UpsertClientProviderRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.UpsertClientProviderRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.UpsertClientProviderRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.UpsertClientProviderRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/umt/clients/{clientId}/entities": {
      "get": {
        "tags": [
          "Clients",
          "PublicEndpoint"
        ],
        "operationId": "umtGetClientEntities",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/supported-idps": {
      "get": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Returns a list of IDPs which are known to be supported by Checkout.\r\n            \r\nWhile IDPs not in the list may still work if they conform to SAML,\r\nthis list represents IDPs that we know will work.",
        "operationId": "getSupportedIdps",
        "responses": {
          "200": {
            "description": "Returns the list of Checkout's known supported IDPs",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.SupportedIdpsResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso": {
      "get": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Returns the SSO configuration for the client.\r\n            \r\nIf the user has 'security:manage' permission, the response will include all SSO configuration information.\r\nIf not, the response will just be a high-level summary of the client's SSO configuration status.",
        "operationId": "getSsoConfiguration",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Returns the SSO configuration for client",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist, or the client hasn't configured SSO.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/status": {
      "get": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Returns the SSO configuration status for the client.",
        "operationId": "getSsoStatus",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Returns the SSO configuration status for client",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoStatusResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist, or the client hasn't configured SSO.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      },
      "put": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Enables/disables SSO login for the client.",
        "operationId": "updateSsoStatus",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoStatusRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoStatusRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoStatusRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoStatusRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If the SSO configuration is invalid for the status change.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "Unprocessable Content",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "501": {
            "description": "If the provided status sso status is false, disable sso isn't supported."
          },
          "403": {
            "description": "If the request has insufficient authorization."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/initiate": {
      "post": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Initiates the SSO configuration process for the client.",
        "operationId": "initiateSsoConfiguration",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SsoConfigurationInitiationRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SsoConfigurationInitiationRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SsoConfigurationInitiationRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SsoConfigurationInitiationRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "SP information for the client to start SSO configuration in their IDP.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.SsoConfigurationInitiationResponse"
                }
              }
            }
          },
          "400": {
            "description": "If the client has already configured SSO.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/idp-metadata": {
      "patch": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Sets the IDP metadata for the client.",
        "operationId": "updateSsoIdpMetadata",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetIdpMetadataRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetIdpMetadataRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetIdpMetadataRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetIdpMetadataRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist or hasn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "Unprocessable Content",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/certificate": {
      "put": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Set/Update the idp certificate",
        "operationId": "updateSsoCertificate",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "required": [
                  "Certificate"
                ],
                "type": "object",
                "properties": {
                  "Certificate": {
                    "type": "string",
                    "format": "binary"
                  }
                }
              },
              "encoding": {
                "Certificate": {
                  "style": "form"
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist or hasn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      },
      "get": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Get the idp certificate",
        "operationId": "getIdpCertificate",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist or certificate not exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "If hasn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/role-mapping": {
      "patch": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Sets the role mapping for the client.",
        "operationId": "updateSsoRoleMapping",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateClientRoleMappingRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateClientRoleMappingRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateClientRoleMappingRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateClientRoleMappingRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "If the client doesn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/entity-mapping-entities": {
      "get": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Gets the entities available for SSO entity mapping for the client.",
        "operationId": "getSsoEntityMappingEntities",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "If the client id is not valid",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/entity-mapping": {
      "patch": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Sets the entity mapping for the client.",
        "operationId": "updateSsoEntityMapping",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntityMappingRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntityMappingRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntityMappingRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntityMappingRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "If the client doesn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/entity-segments-mapping": {
      "put": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Sets the entity segments mapping for the client.",
        "operationId": "updateEntitySegmentsMapping",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntitySegmentsMappingRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntitySegmentsMappingRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntitySegmentsMappingRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntitySegmentsMappingRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "If the client doesn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/test": {
      "put": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Tests the SSO configuration for the client and the currently authorized user.",
        "operationId": "testSso",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.TestSsoConfigurationResponse"
                }
              }
            }
          },
          "400": {
            "description": "If the currently authorized user is not logged in through SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist or hasn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/verified": {
      "put": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Sets whether SSO configuration has been verified, after testing.",
        "operationId": "updateSsoVerificationStatus",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If testing was not completed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist or hasn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/routing/domain-verification-token": {
      "get": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Gets the TXT-record verification token for the client.",
        "operationId": "getSsoRoutingDomainVerificationToken",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The TXT-record verification token for the client",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.GetTxtRecordVerificationIdResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client or domain doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/routing/domains": {
      "put": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Updates the client's SSO domain list.\r\nAll domains will need to be verified through TXT-record validation before they can be used.",
        "operationId": "updateRoutingDomains",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateSsoDomainRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateSsoDomainRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateSsoDomainRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateSsoDomainRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist or hasn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "201": {
            "description": "If the domains added."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/routing/domains/{domain}/verify": {
      "put": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Runs verification for the provided SSO domain.",
        "operationId": "verifySsoRoutingDomain",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "domain",
            "in": "path",
            "description": "The domain to verify.",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The verification status of the domain",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.VerifySsoDomainResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client or domain doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "400": {
            "description": "If the domain is already verified",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/routing/status": {
      "put": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Enables/disables SSO routing rule for the client.",
        "operationId": "updateSsoRoutingStatus",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoRoutingRuleStatusRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoRoutingRuleStatusRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoRoutingRuleStatusRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoRoutingRuleStatusRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist or hasn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/clients/{clientId}/sso/enforce-sso": {
      "patch": {
        "tags": [
          "ClientSSOConfiguration",
          "PublicEndpoint"
        ],
        "summary": "Enforce sso sign in only.",
        "operationId": "updateSsoEnforcementStatus",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.EnforceSsoSignInRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.EnforceSsoSignInRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.EnforceSsoSignInRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.EnforceSsoSignInRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": ""
          },
          "400": {
            "description": "If validation fails",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist or hasn't configured SSO",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "Unprocessable Content",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/clients/{clientId}/custom-roles": {
      "get": {
        "tags": [
          "CustomRoles",
          "PublicEndpoint"
        ],
        "summary": "List custom roles for a client.",
        "operationId": "umtGetClientCustomRoles",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Custom roles for the client",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetCustomRolesResponse"
                }
              }
            }
          },
          "400": {
            "description": "If the request fails validation.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      },
      "post": {
        "tags": [
          "CustomRoles",
          "PublicEndpoint"
        ],
        "summary": "Create custom role for a client.",
        "operationId": "umtCreateClientCustomRoles",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Created custom role",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.CreateCustomRoleResponse"
                }
              }
            }
          },
          "400": {
            "description": "If the request fails validation.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/custom-roles/{customRoleId}": {
      "get": {
        "tags": [
          "CustomRoles",
          "PublicEndpoint"
        ],
        "summary": "Get custom role details.",
        "operationId": "umtGetCustomRole",
        "parameters": [
          {
            "name": "customRoleId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Custom role details",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetCustomRoleResponse"
                }
              }
            }
          },
          "400": {
            "description": "If the request fails validation.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the custom role doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      },
      "put": {
        "tags": [
          "CustomRoles",
          "PublicEndpoint"
        ],
        "summary": "Update custom role.",
        "operationId": "umtUpdateCustomRole",
        "parameters": [
          {
            "name": "customRoleId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "If-Match",
            "in": "header",
            "description": "",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "Custom role updated."
          },
          "400": {
            "description": "If the request fails validation.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the custom role doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      },
      "delete": {
        "tags": [
          "CustomRoles",
          "PublicEndpoint"
        ],
        "summary": "Delete custom role.",
        "operationId": "umtDeleteCustomRole",
        "parameters": [
          {
            "name": "customRoleId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Custom role deleted."
          },
          "400": {
            "description": "If the request fails validation.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the custom role doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/custom-roles/{customRoleId}/replace-role/{replacementRoleId}": {
      "put": {
        "tags": [
          "CustomRoles",
          "PublicEndpoint"
        ],
        "summary": "Replace custom role with another role.",
        "operationId": "umtReplaceCustomRole",
        "parameters": [
          {
            "name": "customRoleId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "replacementRoleId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Custom role replaced."
          },
          "400": {
            "description": "If the request fails validation.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If either custom role doesn't exist",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/fragments/{id}": {
      "get": {
        "tags": [
          "Fragments",
          "PublicEndpoint"
        ],
        "operationId": "getFragment",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          }
        },
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/cat/users/{userId}": {
      "get": {
        "tags": [
          "GetUser"
        ],
        "summary": "Get user details.",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "User details",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Users.Responses.GetUserResponse"
                }
              }
            }
          },
          "404": {
            "description": "User not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/internal/users/{userId}": {
      "get": {
        "tags": [
          "GetUser"
        ],
        "summary": "Get user details.",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "User details",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Users.Responses.GetUserResponse"
                }
              }
            }
          },
          "404": {
            "description": "User not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/cat/users/{userId}/members": {
      "get": {
        "tags": [
          "GetUser"
        ],
        "summary": "Get membership info for user.",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Membership info for user.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Domain.TotalAmountResult`1[UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetUserMembershipsResponse]"
                }
              }
            }
          },
          "404": {
            "description": "User not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/internal/users/{userId}/members": {
      "get": {
        "tags": [
          "GetUser"
        ],
        "summary": "Get membership info for user.",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Membership info for user.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Domain.TotalAmountResult`1[UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetUserMembershipsResponse]"
                }
              }
            }
          },
          "404": {
            "description": "User not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/umt/users/self/mfa/authenticators": {
      "get": {
        "tags": [
          "GetUserAuthenticators",
          "PublicEndpoint"
        ],
        "summary": "Returns list of authenticators and enrolled factors for the user.",
        "operationId": "getUserAuthenticators",
        "responses": {
          "200": {
            "description": "Returns list of authenticators",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.MfaAuthenticator.Authenticator"
                  }
                }
              }
            }
          },
          "403": {
            "description": "Forbidden",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "User not found, or authenticators not found for user",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/": {
      "get": {
        "tags": [
          "Home",
          "PublicEndpoint"
        ],
        "operationId": "rootDiscovery",
        "responses": {
          "200": {
            "description": "OK"
          }
        },
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/internal/internal-users": {
      "post": {
        "tags": [
          "InternalUsers"
        ],
        "summary": "Adds internal users by email and links them to the client.\r\nInserts into InternalUsers and ClientInternalUserMapping tables.",
        "requestBody": {
          "description": "Request containing client id and list of emails.",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.AddInternalUsersRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created"
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/mbc-inline-hook": {
      "post": {
        "tags": [
          "MbcInlineHook",
          "PublicEndpoint"
        ],
        "operationId": "mbcInlineHook",
        "requestBody": {
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/hub-admin-inline-hook": {
      "post": {
        "tags": [
          "MbcInlineHook",
          "PublicEndpoint"
        ],
        "operationId": "mbcHubAdminInlineHook",
        "requestBody": {
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/clients/{clientId}/members": {
      "get": {
        "tags": [
          "Members",
          "PublicEndpoint"
        ],
        "operationId": "umtGetClientMembersAsCsvV2",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "q",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "reportTimeZone",
            "in": "query",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Forbidden",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway"
          },
          "504": {
            "description": "Gateway Timeout"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/clients/{clientId}/members/users-manage": {
      "get": {
        "tags": [
          "Members",
          "PublicEndpoint"
        ],
        "summary": "Get users within a client who have at least one role granting the users:manage permission.",
        "operationId": "umtGetClientMembersWithUsersManagePermission",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "List of users with users:manage permission.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetUsersWithUsersManagePermissionResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetUsersWithUsersManagePermissionResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetUsersWithUsersManagePermissionResponse"
                }
              }
            }
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/clients/{clientId}/members/owner": {
      "put": {
        "tags": [
          "Members",
          "PublicEndpoint"
        ],
        "summary": "Transfer ownership for a client.",
        "operationId": "umtTransferOwnership",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.PutOwnerRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.PutOwnerRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.PutOwnerRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.PutOwnerRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "No Content"
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "200": {
            "description": "Ownership transferred for the client."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/clients/{clientId}/members/{userId}": {
      "delete": {
        "tags": [
          "Members",
          "PublicEndpoint"
        ],
        "summary": "Delete user membership for a client.",
        "operationId": "umtDeleteClientMember",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Membership deleted for the provided user and client."
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/clients/{clientId}/members/{userId}/mfa/reset": {
      "post": {
        "tags": [
          "Members",
          "PublicEndpoint"
        ],
        "summary": "Resets all MFA authentication factors for a user.",
        "operationId": "umtResetClientMemberMfa",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "MFA reset for user."
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "404": {
            "description": "Client or user not found."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/cat/clients/{clientId}/members": {
      "get": {
        "tags": [
          "Members"
        ],
        "summary": "Search members for a client, based on user role.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "roles",
            "in": "query",
            "description": "",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "Skip",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Limit",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "q",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "SortBy",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "SortOrder",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Requests.OktaUserSortOrder"
            }
          },
          {
            "name": "q",
            "in": "query",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The list of users for the client that matched hte provided query",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Domain.TotalMembershipAmountResult`1[UserManagement.WebApi.Services.Members.Models.Member]"
                }
              }
            }
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "post": {
        "tags": [
          "Members"
        ],
        "summary": "Upsert user and the membership for the given client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "User created and membership upserted for the provided client."
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/internal/clients/{clientId}/members": {
      "get": {
        "tags": [
          "Members"
        ],
        "summary": "Search members for a client, based on user role.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "roles",
            "in": "query",
            "description": "",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "Skip",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Limit",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "q",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "SortBy",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "SortOrder",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Requests.OktaUserSortOrder"
            }
          },
          {
            "name": "q",
            "in": "query",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The list of users for the client that matched hte provided query",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Domain.TotalMembershipAmountResult`1[UserManagement.WebApi.Services.Members.Models.Member]"
                }
              }
            }
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "post": {
        "tags": [
          "Members"
        ],
        "summary": "Upsert user and the membership for the given client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "User created and membership upserted for the provided client."
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/cat/clients/{clientId}/members/{userId}": {
      "get": {
        "tags": [
          "Members"
        ],
        "summary": "Get user details for a member of a client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Membership details for the provided user and client",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetMemberResponse"
                }
              }
            }
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "put": {
        "tags": [
          "Members"
        ],
        "summary": "Upsert user membership for a client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "Membership upserted for the provided user and client."
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "delete": {
        "tags": [
          "Members"
        ],
        "summary": "Delete user membership for a client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Membership deleted for the provided user and client."
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/internal/clients/{clientId}/members/{userId}": {
      "get": {
        "tags": [
          "Members"
        ],
        "summary": "Get user details for a member of a client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Membership details for the provided user and client",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetMemberResponse"
                }
              }
            }
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "put": {
        "tags": [
          "Members"
        ],
        "summary": "Upsert user membership for a client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "Membership upserted for the provided user and client."
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "delete": {
        "tags": [
          "Members"
        ],
        "summary": "Delete user membership for a client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Membership deleted for the provided user and client."
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/cat/clients/{clientId}/members/owner": {
      "put": {
        "tags": [
          "Members"
        ],
        "summary": "Transfer ownership for a client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Ownership transferred for the client.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.UpdateMemberResponse"
                }
              }
            }
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/internal/clients/{clientId}/members/owner": {
      "put": {
        "tags": [
          "Members"
        ],
        "summary": "Transfer ownership for a client.",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Ownership transferred for the client.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.UpdateMemberResponse"
                }
              }
            }
          },
          "400": {
            "description": "Request validation failed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Client or user not found.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/internal/users/migrate-okta-user-id": {
      "put": {
        "tags": [
          "MigrateOktaUserId"
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.MigrateOktaUserReferenceRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.MigrateOktaUserReferenceRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.MigrateOktaUserReferenceRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.MigrateOktaUserReferenceRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/okta-inline-hook": {
      "post": {
        "tags": [
          "OktaInlineHook",
          "PublicEndpoint"
        ],
        "summary": "To debug this endpoint locally:\r\n1- From okta, add a user to the group \"inline_hook_degug\"\r\n2- From CLI, run ngrok with: $> ngrok http --subdomain=checkout-okta --region=eu 5051\r\n3- Run API locally\r\n4- Access token request for user will be routed to https://checkout-okta.eu.ngrok.io tunneled to http://localhost:5000",
        "operationId": "oktaInlineHook",
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Responses.Models.OktaInlineHookResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/.well-known/client-roles": {
      "get": {
        "tags": [
          "Roles",
          "PublicEndpoint"
        ],
        "summary": "Returns a list of client roles available for use by default, with the permissions\r\nassociated to each role.",
        "operationId": "getClientRoles",
        "responses": {
          "200": {
            "description": "List of available client roles.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.ClientRolesResponse"
                }
              }
            }
          }
        },
        "x-egw-api": "usermanagement-api"
      }
    },
    "/.well-known/custom-roles/permissions": {
      "get": {
        "tags": [
          "Roles",
          "PublicEndpoint"
        ],
        "summary": "Returns a list of permissions which can be assigned to custom roles.",
        "operationId": "getCustomRolesPermissions",
        "responses": {
          "200": {
            "description": "List of permissions available for custom roles.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.CustomRolesPermissionsResponse"
                }
              }
            }
          }
        },
        "x-egw-api": "usermanagement-api"
      }
    },
    "/.well-known/permission-groups": {
      "get": {
        "tags": [
          "Roles",
          "PublicEndpoint"
        ],
        "summary": "Returns a list of permission groups, each with its mapped permissions.",
        "operationId": "getPermissionGroups",
        "responses": {
          "200": {
            "description": "Returns permission groups and their permissions.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.PermissionGroupDto"
                  }
                }
              }
            }
          }
        },
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/cat/clients/{clientId}/entities/{entityId}/segments/{segmentId}": {
      "get": {
        "tags": [
          "Segments"
        ],
        "operationId": "getEntitySegment",
        "parameters": [
          {
            "name": "segmentId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "clientId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "entityId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetSegmentResponse"
                }
              }
            }
          },
          "404": {
            "description": "Not Found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "put": {
        "tags": [
          "Segments"
        ],
        "operationId": "putEntitySegment",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "entityId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "segmentId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutSegmentRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutSegmentRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutSegmentRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutSegmentRequest"
              }
            }
          }
        },
        "responses": {
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "204": {
            "description": "No Content"
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "409": {
            "description": "Conflict",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "delete": {
        "tags": [
          "Segments"
        ],
        "operationId": "deleteEntitySegment",
        "parameters": [
          {
            "name": "segmentId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "clientId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "entityId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "204": {
            "description": "No Content"
          },
          "404": {
            "description": "Not Found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/migration/sso-service-init/mismatches": {
      "get": {
        "tags": [
          "SsoServiceInitMigration"
        ],
        "parameters": [
          {
            "name": "pageLimit",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 30
            }
          },
          {
            "name": "pageIndex",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/migration/sso-service-init/fix": {
      "post": {
        "tags": [
          "SsoServiceInitMigration"
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatch"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatch"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatch"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatch"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/mfa/enrollment/enforce": {
      "post": {
        "tags": [
          "TempMfaEnforcement"
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/mfa/enrollment/revert": {
      "post": {
        "tags": [
          "TempMfaEnforcement"
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/mfa/enrollment/progress": {
      "get": {
        "tags": [
          "TempMfaEnforcement"
        ],
        "parameters": [
          {
            "name": "clientId",
            "in": "query",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/umt/users/mfa/update-enrollment-hook": {
      "post": {
        "tags": [
          "UpdateMfaEnrollmentHook",
          "PublicEndpoint"
        ],
        "summary": "Okta event hook to update okta profile MFA enrollment status\r\nFor Local testing, run ngrok with: $> ngrok http --subdomain=checkout-okta --region=eu 5051",
        "operationId": "updateMfaEnrollmentEventHook",
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      },
      "get": {
        "tags": [
          "UpdateMfaEnrollmentHook",
          "PublicEndpoint"
        ],
        "summary": "https://developer.okta.com/docs/concepts/event-hooks/#one-time-verification-request",
        "operationId": "updateMfaEnrollmentEventHookOneTimeVerification",
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/api/user-entitlements": {
      "get": {
        "tags": [
          "UserEntitlements"
        ],
        "summary": "Get all user entitlements that match one or more filters",
        "operationId": "GetAllUserEntitlements",
        "parameters": [
          {
            "name": "entity_scope",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "email",
            "in": "query",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Responses.GetUserEntitlementsResponse"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      },
      "delete": {
        "tags": [
          "UserEntitlements"
        ],
        "summary": "Delete user entitlements for a single email",
        "operationId": "DeleteUserEntitlements",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Requests.DeleteUserEntitlements"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "User entitlements deleted"
          },
          "400": {
            "description": "Bad request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "Email not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/user-entitlements/bulk": {
      "post": {
        "tags": [
          "UserEntitlements"
        ],
        "summary": "Bulk create user entitlements",
        "operationId": "CreateMultipleUserEntitlements",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Requests.CreateUserEntitlements"
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "User entitlements Created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Responses.GetUserEntitlementsResponse"
                }
              }
            }
          },
          "400": {
            "description": "Bad request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/user-onboarding/clients/{clientId}/entities/{entityId}/appliers": {
      "put": {
        "tags": [
          "UserOnboarding"
        ],
        "summary": "Upsert user in applier role. Creates user if user does not exist.\r\nAssign applier role if user exists.",
        "operationId": "userOnboardingUpsertAppliersForEntity",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "entityId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Upsert result.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Responses.UpsertOnboardingUserResponse"
                }
              }
            }
          },
          "400": {
            "description": "If request is malformed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "500": {
            "description": "Internal Server Error"
          },
          "404": {
            "description": "If the client or entity doesn't exist."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/user-onboarding/clients/{clientId}/entities/{entityId}/owner": {
      "put": {
        "tags": [
          "UserOnboarding"
        ],
        "summary": "Upsert user in owner role. Creates user if user does not exist.\r\nAssign owner role if user exists.",
        "operationId": "userOnboardingUpdateOwner",
        "parameters": [
          {
            "name": "clientId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "entityId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Responses.UpsertOnboardingUserResponse"
                }
              }
            }
          },
          "400": {
            "description": "If request is malformed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If the request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If the client or entity doesn't exist.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "200": {
            "description": "Upsert result."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/api/user-onboarding/sub-entities/{subentityId}/appliers": {
      "put": {
        "tags": [
          "UserOnboarding"
        ],
        "summary": "Upsert user in applier role as a member of sub-entity (seller). Creates user if user does not exist.\r\nAssign applier role if user exists.",
        "operationId": "userOnboardingUpdateAppliersForSubEntity",
        "parameters": [
          {
            "name": "subentityId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Upsert result.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserOnboarding.Responses.UpsertOnboardingUserResponse"
                }
              }
            }
          },
          "400": {
            "description": "If request is malformed.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "403": {
            "description": "If request has insufficient authorization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "404": {
            "description": "If entity doesn't exist.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "If server error."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "ApiKeyAuth": [ ]
          }
        ]
      }
    },
    "/umt/users/self": {
      "get": {
        "tags": [
          "Users",
          "PublicEndpoint"
        ],
        "summary": "Get information about the currently authenticated user.",
        "operationId": "umtGetSelf",
        "responses": {
          "200": {
            "description": "Information about the currently authenticated user.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetCurrentUserResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetCurrentUserResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetCurrentUserResponse"
                }
              }
            }
          },
          "404": {
            "description": "User not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/users/{userId}": {
      "put": {
        "tags": [
          "Users",
          "PublicEndpoint"
        ],
        "summary": "Update user details.",
        "operationId": "umtUpdateUser",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpdateUserRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpdateUserRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpdateUserRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpdateUserRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "User details updated"
          },
          "404": {
            "description": "User not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/users/{userId}/password": {
      "put": {
        "tags": [
          "Users",
          "PublicEndpoint"
        ],
        "summary": "Update user password.",
        "operationId": "umtUpdateUserPassword",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json-patch+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.ChangePasswordRequest"
              }
            },
            "application/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.ChangePasswordRequest"
              }
            },
            "text/json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.ChangePasswordRequest"
              }
            },
            "application/*+json; version=1.0": {
              "schema": {
                "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Requests.ChangePasswordRequest"
              }
            }
          }
        },
        "responses": {
          "204": {
            "description": "User password updated"
          },
          "404": {
            "description": "User not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/users/{userId}/activate": {
      "post": {
        "tags": [
          "Users",
          "PublicEndpoint"
        ],
        "summary": "Trigger activation for user.",
        "operationId": "umtTriggerUserActivation",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "User activation triggered."
          },
          "404": {
            "description": "User not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/users/{userId}/unlock": {
      "post": {
        "tags": [
          "Users",
          "PublicEndpoint"
        ],
        "summary": "Unlock user.",
        "operationId": "umtUnlockUser",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "User unlocked."
          },
          "404": {
            "description": "User not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Access.Common.Api.Models.ErrorResponse"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/users/{userId}/suspend": {
      "post": {
        "tags": [
          "Users",
          "PublicEndpoint"
        ],
        "summary": "Suspend user.",
        "operationId": "umtSuspendUser",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "User suspended."
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "404": {
            "description": "User not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "Unprocessable entity.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    },
    "/umt/users/{userId}/unsuspend": {
      "post": {
        "tags": [
          "Users",
          "PublicEndpoint"
        ],
        "summary": "Unsuspend user.",
        "operationId": "umtUnsuspendUser",
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "User suspended."
          },
          "403": {
            "description": "Invalid authorization.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "404": {
            "description": "User not found.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "422": {
            "description": "Unprocessable entity.",
            "content": {
              "text/plain; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "application/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              },
              "text/json; version=1.0": {
                "schema": {
                  "$ref": "#/components/schemas/Microsoft.AspNetCore.Mvc.ProblemDetails"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error."
          },
          "502": {
            "description": "Bad Gateway."
          },
          "504": {
            "description": "Request timeout."
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "security": [
          {
            "Bearer": [ ]
          }
        ],
        "x-egw-api": "usermanagement-api"
      }
    }
  },
  "components": {
    "schemas": {
      "Access.Common.Api.Models.ErrorResponse": {
        "type": "object",
        "properties": {
          "request_id": {
            "type": "string",
            "nullable": true
          },
          "error_type": {
            "type": "string",
            "nullable": true
          },
          "error_codes": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "Checkout.Common.WebApi.Models.Link": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "href": {
            "type": "string",
            "nullable": true
          },
          "templated": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "Microsoft.AspNetCore.Mvc.ProblemDetails": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "nullable": true
          },
          "title": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "nullable": true
          },
          "detail": {
            "type": "string",
            "nullable": true
          },
          "instance": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": { }
      },
      "Optional.Option`1[System.DateTimeOffset]": {
        "type": "object",
        "properties": {
          "has_value": {
            "type": "boolean",
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "Optional.Option`1[System.DateTime]": {
        "type": "object",
        "properties": {
          "has_value": {
            "type": "boolean",
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.OktaInlineHook.Domain.PaymentServiceProvider.PaymentServiceProviderEnum": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "format": "int32"
      },
      "UserManagement.OktaInlineHook.Domain.Segments.EntitySegments": {
        "type": "object",
        "properties": {
          "has_any_access": {
            "type": "boolean",
            "readOnly": true
          },
          "has_only_full_access_to_entities": {
            "type": "boolean",
            "readOnly": true
          },
          "entity_ids": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.OktaInlineHook.Domain.ValueObjects.Ids.EntityId"
            },
            "nullable": true,
            "readOnly": true
          },
          "full_access_entity_ids": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.OktaInlineHook.Domain.ValueObjects.Ids.EntityId"
            },
            "nullable": true,
            "readOnly": true
          },
          "limited_access_segments": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "readOnly": true
          },
          "value": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "example": "*"
            },
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.OktaInlineHook.Domain.ValueObjects.Ids.EntityId": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.ClientSSOConfiguration.Models.EntitiesAccess.EntityAccess": {
        "type": "object",
        "properties": {
          "entity_id": {
            "type": "string",
            "nullable": true
          },
          "is_full_access": {
            "type": "boolean"
          },
          "segment_dimension_hashes": {
            "uniqueItems": true,
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.ClientSSOConfiguration.Models.EntitiesAccess.SamlValueEntitiesMapping": {
        "type": "object",
        "properties": {
          "saml_value": {
            "type": "string",
            "nullable": true
          },
          "entities": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.ClientSSOConfiguration.Models.EntitiesAccess.EntityAccess"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Requests.AddInternalUsersRequest": {
        "type": "object",
        "properties": {
          "client_id": {
            "type": "string",
            "description": "The client identifier (string CKO client id).",
            "nullable": true
          },
          "emails": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of email addresses to add as internal users for the client.",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Requests.CreateUserAndMemberRequest": {
        "type": "object",
        "properties": {
          "user": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Models.Requests.CreateUserRequestV2"
          },
          "membership": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Requests.MigrateOktaUserReferenceRequest": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutMemberRequest": {
        "type": "object",
        "properties": {
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          },
          "entities": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "deprecated": true
          },
          "entity_segments": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "nullable": true,
              "example": "*"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutOwnerRequest": {
        "type": "object",
        "properties": {
          "source_user_id": {
            "type": "string",
            "nullable": true
          },
          "target_user_id": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Requests.PutSegmentRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "dimension_hash": {
            "type": "string",
            "nullable": true
          },
          "brand": {
            "type": "string",
            "nullable": true
          },
          "business_category": {
            "type": "string",
            "nullable": true
          },
          "market": {
            "type": "string",
            "nullable": true
          },
          "processing_channel_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          },
          "status": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.Segments.SegmentStatus"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Requests.UpsertClientProviderRequest": {
        "type": "object",
        "properties": {
          "provider_enum": {
            "$ref": "#/components/schemas/UserManagement.OktaInlineHook.Domain.PaymentServiceProvider.PaymentServiceProviderEnum"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Responses.ActivateUserResponse": {
        "type": "object",
        "properties": {
          "activation_url": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetMemberDiscovery": {
        "type": "object",
        "properties": {
          "owner": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "self": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "curies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
            },
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetMemberResponse": {
        "type": "object",
        "properties": {
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "readOnly": true
          },
          "_embedded": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Users.Responses.GetUsersResponse.UserItem"
          },
          "user_id": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "client_id": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "entities": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "readOnly": true
          },
          "entity_segments": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "nullable": true,
              "example": "*"
            },
            "nullable": true,
            "readOnly": true
          },
          "permissions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.PermissionDto"
            },
            "nullable": true,
            "readOnly": true
          },
          "date_created": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "date_modified": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "_links": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetMemberDiscovery"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetSegmentResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "entity_id": {
            "type": "string",
            "nullable": true
          },
          "client_id": {
            "type": "string",
            "nullable": true
          },
          "dimension_hash": {
            "type": "string",
            "nullable": true
          },
          "brand": {
            "type": "string",
            "nullable": true
          },
          "business_category": {
            "type": "string",
            "nullable": true
          },
          "market": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.Segments.SegmentStatus"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetUserMembershipsResponse": {
        "type": "object",
        "properties": {
          "client_id": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "readOnly": true
          },
          "entities": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "readOnly": true,
            "deprecated": true
          },
          "entity_segments": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "nullable": true,
              "example": "*"
            },
            "nullable": true,
            "readOnly": true
          },
          "date_created": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "date_modified": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "_links": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetMemberDiscovery"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Responses.UpdateMemberDiscovery": {
        "type": "object",
        "properties": {
          "prev": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "self": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "curies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
            },
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientAdminTool.Responses.UpdateMemberResponse": {
        "type": "object",
        "properties": {
          "_links": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.UpdateMemberDiscovery"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.EnforceSsoSignInRequest": {
        "required": [
          "enforce"
        ],
        "type": "object",
        "properties": {
          "enforce": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetIdpMetadataRequest": {
        "required": [
          "issuer",
          "sso_url"
        ],
        "type": "object",
        "properties": {
          "issuer": {
            "minLength": 1,
            "type": "string"
          },
          "sso_url": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoRoutingRuleStatusRequest": {
        "required": [
          "enabled"
        ],
        "type": "object",
        "properties": {
          "enabled": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SetSsoStatusRequest": {
        "required": [
          "enabled"
        ],
        "type": "object",
        "properties": {
          "enabled": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.SsoConfigurationInitiationRequest": {
        "required": [
          "idp_provider"
        ],
        "type": "object",
        "properties": {
          "idp_provider": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateClientRoleMappingRequest": {
        "required": [
          "idp_attribute_to_role_id_mapping"
        ],
        "type": "object",
        "properties": {
          "idp_attribute_to_role_id_mapping": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "nullable": true
            }
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntityMappingRequest": {
        "required": [
          "use_entity_mapping_restrictions"
        ],
        "type": "object",
        "properties": {
          "idp_attribute_to_entity_ids_mapping": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "nullable": true
            },
            "nullable": true
          },
          "use_entity_mapping_restrictions": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateEntitySegmentsMappingRequest": {
        "required": [
          "use_entity_mapping_restrictions"
        ],
        "type": "object",
        "properties": {
          "use_entity_mapping_restrictions": {
            "type": "string"
          },
          "saml_value_entities_mappings": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.ClientSSOConfiguration.Models.EntitiesAccess.SamlValueEntitiesMapping"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Requests.UpdateSsoDomainRequest": {
        "required": [
          "domains"
        ],
        "type": "object",
        "properties": {
          "domains": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "is_domain_purge_confirmed": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse": {
        "type": "object",
        "properties": {
          "idp_provider": {
            "type": "string",
            "nullable": true
          },
          "enabled": {
            "type": "boolean"
          },
          "routing": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.RoutingDto"
          },
          "tested": {
            "type": "boolean"
          },
          "verified": {
            "type": "boolean"
          },
          "enforce_sso_sign_in": {
            "type": "boolean"
          },
          "sp_metadata": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.SpMetadataDto"
          },
          "idp_metadata": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.IdpMetadataDto"
          },
          "use_entity_mapping_restrictions": {
            "type": "boolean"
          },
          "idp_attribute_to_entity_ids_mapping": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "nullable": true
            },
            "nullable": true
          },
          "idp_attribute_to_entity_access_mappings": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.SamlAttributeToEntityAccessMapping"
            },
            "nullable": true
          },
          "idp_attribute_to_role_id_mapping": {
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "nullable": true
            },
            "nullable": true
          },
          "configuration_initiated_at": {
            "type": "string",
            "format": "date-time"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.IdpMetadataDto": {
        "type": "object",
        "properties": {
          "issuer": {
            "type": "string",
            "nullable": true
          },
          "sso_url": {
            "type": "string",
            "nullable": true
          },
          "certificate_expiration": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.RoutingDomainDto": {
        "type": "object",
        "properties": {
          "domain": {
            "type": "string",
            "nullable": true
          },
          "verified": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.RoutingDto": {
        "type": "object",
        "properties": {
          "enabled": {
            "type": "boolean"
          },
          "last_updated_at": {
            "type": "string",
            "nullable": true
          },
          "domains": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.RoutingDomainDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.SamlAttributeToEntityAccessMapping": {
        "type": "object",
        "properties": {
          "saml_attribute": {
            "type": "string",
            "nullable": true
          },
          "entity_access": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {
                "type": "string",
                "example": "*"
              }
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoConfigurationResponse.SpMetadataDto": {
        "type": "object",
        "properties": {
          "acs_url": {
            "type": "string",
            "nullable": true
          },
          "audience_uri": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.ClientSsoStatusResponse": {
        "type": "object",
        "properties": {
          "enabled": {
            "type": "boolean"
          },
          "tested": {
            "type": "boolean"
          },
          "verified": {
            "type": "boolean"
          },
          "routing_enabled": {
            "type": "boolean"
          },
          "enforce_sso_sign_in": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.GetTxtRecordVerificationIdResponse": {
        "type": "object",
        "properties": {
          "txt_record_verification_id": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.SsoConfigurationInitiationResponse": {
        "type": "object",
        "properties": {
          "acs_url": {
            "type": "string",
            "format": "uri",
            "nullable": true
          },
          "audience_uri": {
            "type": "string",
            "format": "uri",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.SupportedIdpsResponse": {
        "type": "object",
        "properties": {
          "supported_idps": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.TestSsoConfigurationResponse": {
        "type": "object",
        "properties": {
          "user_id": {
            "type": "string",
            "nullable": true
          },
          "email": {
            "type": "string",
            "nullable": true
          },
          "first_name": {
            "type": "string",
            "nullable": true
          },
          "last_name": {
            "type": "string",
            "nullable": true
          },
          "entities": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.ClientSSOConfiguration.Responses.VerifySsoDomainResponse": {
        "type": "object",
        "properties": {
          "domain": {
            "type": "string",
            "nullable": true
          },
          "verified": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest": {
        "type": "object",
        "properties": {
          "eventType": {
            "type": "string",
            "nullable": true
          },
          "eventTypeVersion": {
            "type": "string",
            "nullable": true
          },
          "cloudEventsVersion": {
            "type": "string",
            "nullable": true
          },
          "source": {
            "type": "string",
            "nullable": true
          },
          "eventId": {
            "type": "string",
            "nullable": true
          },
          "eventTime": {
            "type": "string",
            "nullable": true
          },
          "contenType": {
            "type": "string",
            "nullable": true
          },
          "data": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.OktaEventData"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.ActorOrTarget": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "nullable": true
          },
          "alternateId": {
            "type": "string",
            "nullable": true
          },
          "displayName": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.AuthenticationContext": {
        "type": "object",
        "properties": {
          "authenticationStep": {
            "type": "integer",
            "format": "int64"
          },
          "externalSessionId": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.Client": {
        "type": "object",
        "properties": {
          "zone": {
            "type": "string",
            "nullable": true
          },
          "device": {
            "type": "string",
            "nullable": true
          },
          "userAgent": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.UserAgent"
          },
          "ipAddress": {
            "type": "string",
            "nullable": true
          },
          "geographicalContext": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.GeographicalContext"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.DebugContext": {
        "type": "object",
        "properties": {
          "debugData": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.DebugData"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.DebugData": {
        "type": "object",
        "properties": {
          "requestUri": {
            "type": "string",
            "nullable": true
          },
          "requestId": {
            "type": "string",
            "nullable": true
          },
          "origin": {
            "type": "string",
            "nullable": true
          },
          "factor": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.GeographicalContext": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "nullable": true
          },
          "state": {
            "type": "string",
            "nullable": true
          },
          "country": {
            "type": "string",
            "nullable": true
          },
          "postalCode": {
            "type": "string",
            "nullable": true
          },
          "geolocation": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.Geolocation"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.Geolocation": {
        "type": "object",
        "properties": {
          "lat": {
            "type": "number",
            "format": "double"
          },
          "lon": {
            "type": "number",
            "format": "double"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.OktaEvent": {
        "type": "object",
        "properties": {
          "version": {
            "type": "string",
            "nullable": true
          },
          "severity": {
            "type": "string",
            "nullable": true
          },
          "client": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.Client"
          },
          "actor": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.ActorOrTarget"
          },
          "target": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.ActorOrTarget"
            },
            "nullable": true
          },
          "outcome": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.Outcome"
          },
          "uuid": {
            "type": "string",
            "format": "uuid"
          },
          "published": {
            "type": "string",
            "nullable": true
          },
          "eventType": {
            "type": "string",
            "nullable": true
          },
          "displayMessage": {
            "type": "string",
            "nullable": true
          },
          "transaction": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.Transaction"
          },
          "debugContext": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.DebugContext"
          },
          "legacyEventType": {
            "type": "string",
            "nullable": true
          },
          "authenticationContext": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.AuthenticationContext"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.OktaEventData": {
        "type": "object",
        "properties": {
          "events": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.OktaEvent"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.Outcome": {
        "type": "object",
        "properties": {
          "result": {
            "type": "string",
            "nullable": true
          },
          "reason": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.Transaction": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "nullable": true
          },
          "id": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaEventHook.Requests.OktaEventRequest.UserAgent": {
        "type": "object",
        "properties": {
          "os": {
            "type": "string",
            "nullable": true
          },
          "browser": {
            "type": "string",
            "nullable": true
          },
          "rawUserAgent": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest": {
        "type": "object",
        "properties": {
          "data": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData": {
        "type": "object",
        "properties": {
          "context": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext"
          },
          "identity": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaIdToken"
          },
          "access": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaAccessToken"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaAccessToken": {
        "type": "object",
        "properties": {
          "claims": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaAccessToken.OktaAccessClaims"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaAccessToken.OktaAccessClaims": {
        "type": "object",
        "properties": {
          "jti": {
            "type": "string",
            "nullable": true
          },
          "isInternal": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext": {
        "type": "object",
        "properties": {
          "protocol": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaProtocol"
          },
          "session": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaSession"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaProtocol": {
        "type": "object",
        "properties": {
          "request": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaProtocol.OktaRequest"
          },
          "client": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaProtocol.OktaClient"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaProtocol.OktaClient": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaProtocol.OktaRequest": {
        "type": "object",
        "properties": {
          "state": {
            "type": "string",
            "description": "State possibly encoded by the Hub front-end with",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaSession": {
        "type": "object",
        "properties": {
          "userId": {
            "type": "string",
            "description": "Okta User ID",
            "nullable": true
          },
          "login": {
            "type": "string",
            "description": "User email",
            "nullable": true
          },
          "idp": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaSession.OktaIdp"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaContext.OktaSession.OktaIdp": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaIdToken": {
        "type": "object",
        "properties": {
          "claims": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaIdToken.OktaIdentityClaims"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Requests.OktaInlineHookRequest.OktaData.OktaIdToken.OktaIdentityClaims": {
        "type": "object",
        "properties": {
          "idpGroups": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Custom claim to hold Client user IDP groups",
            "nullable": true
          },
          "idpEntities": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Custom claim to hold Client user IDP entities",
            "nullable": true
          },
          "spGroups": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Custom claim to hold SP groups used as roles for Internal User",
            "nullable": true
          },
          "isInternal": {
            "type": "string",
            "description": "Custom claim that dictates if the subject is Client user or an Internal user\r\nOnly set to true for CKO users through checkout.okta.com federation",
            "nullable": true
          },
          "jti": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Responses.Models.Command": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "nullable": true
          },
          "value": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Responses.Models.TokenOperation"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Responses.Models.OktaInlineHookResponse": {
        "type": "object",
        "properties": {
          "debugContext": {
            "type": "object",
            "additionalProperties": {
              "nullable": true
            },
            "nullable": true
          },
          "commands": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.OktaInlineHook.Responses.Models.Command"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.OktaInlineHook.Responses.Models.TokenOperation": {
        "type": "object",
        "properties": {
          "op": {
            "type": "string",
            "nullable": true
          },
          "path": {
            "type": "string",
            "nullable": true
          },
          "value": {
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Requests.OktaUserSortOrder": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "format": "int32"
      },
      "UserManagement.WebApi.Controllers.Responses.ClientRolesResponse": {
        "type": "object",
        "properties": {
          "roles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.RoleDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Responses.CustomRolesPermissionsResponse": {
        "type": "object",
        "properties": {
          "permissions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.PermissionDto"
            },
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Responses.PermissionDetailDto": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "is_custom_role_allowed": {
            "type": "boolean"
          },
          "custom_role_restriction_message": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Responses.PermissionDto": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Responses.PermissionGroupDto": {
        "type": "object",
        "properties": {
          "group_id": {
            "type": "integer",
            "format": "int32"
          },
          "group_name": {
            "type": "string",
            "nullable": true
          },
          "permissions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.PermissionDetailDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Responses.RoleDto": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "permissions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.PermissionDto"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatch": {
        "type": "object",
        "properties": {
          "to_enable": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatchItem"
            },
            "nullable": true
          },
          "to_disable": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatchItem"
            },
            "nullable": true
          },
          "in_sync": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatchItem"
            },
            "nullable": true
          },
          "failed": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatchItem"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.SsoMigration.Responses.SsoMigrationMismatchItem": {
        "type": "object",
        "properties": {
          "cko_client_id": {
            "type": "string",
            "nullable": true
          },
          "okta_idp_id": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserEntitlements.Requests.CreateEntitlement": {
        "required": [
          "client_id",
          "entity_id",
          "type"
        ],
        "type": "object",
        "properties": {
          "type": {
            "minLength": 1,
            "type": "string",
            "example": "AUTHORISED_SIGNATORY or DELEGATED_SIGNATORY"
          },
          "client_id": {
            "minLength": 1,
            "type": "string"
          },
          "entity_id": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserEntitlements.Requests.CreateUserEntitlements": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "nullable": true
          },
          "entitlements": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Requests.CreateEntitlement"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserEntitlements.Requests.DeleteEntitlement": {
        "required": [
          "client_id",
          "entity_id",
          "type"
        ],
        "type": "object",
        "properties": {
          "type": {
            "minLength": 1,
            "type": "string"
          },
          "client_id": {
            "minLength": 1,
            "type": "string"
          },
          "entity_id": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserEntitlements.Requests.DeleteUserEntitlements": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "nullable": true
          },
          "entitlements": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Requests.DeleteEntitlement"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserEntitlements.Responses.Entitlement": {
        "required": [
          "client_id",
          "entity_id",
          "type"
        ],
        "type": "object",
        "properties": {
          "type": {
            "minLength": 1,
            "type": "string"
          },
          "client_id": {
            "minLength": 1,
            "type": "string"
          },
          "entity_id": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserEntitlements.Responses.GetUserEntitlementsResponse": {
        "required": [
          "data",
          "total"
        ],
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Responses.UserEntitlements"
            }
          },
          "total": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserEntitlements.Responses.UserEntitlements": {
        "required": [
          "email",
          "entitlements"
        ],
        "type": "object",
        "properties": {
          "email": {
            "minLength": 1,
            "type": "string"
          },
          "entitlements": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Responses.Entitlement"
            }
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Requests.ChangePasswordRequest": {
        "type": "object",
        "properties": {
          "old_password": {
            "type": "string",
            "nullable": true
          },
          "new_password": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Requests.PutOwnerRequest": {
        "type": "object",
        "properties": {
          "target_user_id": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpdateUserRequest": {
        "type": "object",
        "properties": {
          "first_name": {
            "type": "string",
            "nullable": true
          },
          "last_name": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Requests.UpsertCustomRoleRequest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "permissions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Responses.CreateCustomRoleResponse": {
        "type": "object",
        "properties": {
          "_links": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.CustomRoleDiscovery"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Responses.CustomRoleDiscovery": {
        "type": "object",
        "properties": {
          "self": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "curies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
            },
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetCurrentUserResponse": {
        "type": "object",
        "properties": {
          "current_role_names": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          },
          "user_entitlements": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserEntitlements.Responses.Entitlement"
            },
            "nullable": true
          },
          "first_name": {
            "type": "string",
            "nullable": true
          },
          "last_name": {
            "type": "string",
            "nullable": true
          },
          "email": {
            "type": "string",
            "nullable": true
          },
          "user_id": {
            "type": "string",
            "nullable": true
          },
          "is_federated": {
            "type": "boolean"
          },
          "_links": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Users.Responses.UserDiscovery"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetCustomRoleResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "permissions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.PermissionDto"
            },
            "nullable": true
          },
          "_links": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.CustomRoleDiscovery"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetCustomRolesResponse": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Responses.RoleDto"
            },
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Responses.GetUsersWithUsersManagePermissionResponse": {
        "type": "object",
        "properties": {
          "admin_users": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.UserManagementTool.Responses.UserWithUsersManagePermissionItem"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserManagementTool.Responses.UserWithUsersManagePermissionItem": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "nullable": true
          },
          "first_name": {
            "type": "string",
            "nullable": true
          },
          "last_name": {
            "type": "string",
            "nullable": true
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          },
          "last_login": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserOnboarding.Requests.UpsertOnboardingUserRequest": {
        "required": [
          "email"
        ],
        "type": "object",
        "properties": {
          "email": {
            "minLength": 1,
            "type": "string"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.UserOnboarding.Responses.UpsertOnboardingUserResponse": {
        "type": "object",
        "properties": {
          "user_id": {
            "type": "string",
            "nullable": true
          },
          "is_existing_user": {
            "type": "boolean"
          },
          "is_active_user": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Users.Responses.GetUserResponse": {
        "type": "object",
        "properties": {
          "first_name": {
            "type": "string",
            "nullable": true
          },
          "last_name": {
            "type": "string",
            "nullable": true
          },
          "email": {
            "type": "string",
            "nullable": true
          },
          "user_id": {
            "type": "string",
            "nullable": true
          },
          "is_federated": {
            "type": "boolean"
          },
          "_links": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.Users.Responses.UserDiscovery"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Users.Responses.GetUsersResponse.UserItem": {
        "type": "object",
        "properties": {
          "user_id": {
            "type": "string",
            "nullable": true
          },
          "first_name": {
            "type": "string",
            "nullable": true
          },
          "last_name": {
            "type": "string",
            "nullable": true
          },
          "email": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "nullable": true
          },
          "is_federated": {
            "type": "boolean"
          },
          "date_created": {
            "type": "string",
            "nullable": true
          },
          "date_modified": {
            "type": "string",
            "nullable": true
          },
          "last_login": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Controllers.Users.Responses.UserDiscovery": {
        "type": "object",
        "properties": {
          "usr:activate": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "usr:change-password": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "usr:members": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "self": {
            "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
          },
          "curies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Checkout.Common.WebApi.Models.Link"
            },
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Domain.CkoClientId": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Domain.Email": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Domain.FirstName": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Domain.LastName": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Domain.OktaUserId": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Domain.Role": {
        "type": "object",
        "properties": {
          "id_string": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "permissions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "readOnly": true
          },
          "user_managed": {
            "type": "boolean",
            "description": "If a role is \"user managed\", it can be manually assigned via Dashboard or CAT.\r\n            \r\nOtherwise, it can only be assigned systemically (e.g. via an API call from an internal service)."
          }
        },
        "additionalProperties": false,
        "description": "Base class for role assignment of either fixed roles or custom roles"
      },
      "UserManagement.WebApi.Domain.Segments.SegmentStatus": {
        "enum": [
          0,
          1
        ],
        "type": "integer",
        "format": "int32"
      },
      "UserManagement.WebApi.Domain.TotalAmountResult`1[UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetUserMembershipsResponse]": {
        "type": "object",
        "properties": {
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Controllers.ClientAdminTool.Responses.GetUserMembershipsResponse"
            },
            "nullable": true
          },
          "total_amount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Domain.TotalMembershipAmountResult`1[UserManagement.WebApi.Services.Members.Models.Member]": {
        "type": "object",
        "properties": {
          "unfiltered_total_count": {
            "type": "integer",
            "format": "int32"
          },
          "items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Services.Members.Models.Member"
            },
            "nullable": true
          },
          "total_amount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false,
        "description": "This method is intended to use when member search made with a filter. In this case UnfilteredTotalCount indicates total member count of the client,\r\nand TotalAmount for the count of the search result. If there is no filter, both values are equal.\r\ne.g. If a client has 3 members, and 1 member matches the search term, then the total_count will be 1, as we will return 1 member on the response. \r\nAnd the unfiltered_total_count will be 3, as this client has 3 memberships regardless of the search."
      },
      "UserManagement.WebApi.Domain.UserId": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Domain.UserStatus": {
        "enum": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8
        ],
        "type": "integer",
        "description": "An enumeration of UserStatus values. See details https://developer.okta.com/docs/reference/api/users/#user-status",
        "format": "int32"
      },
      "UserManagement.WebApi.Mfa.MfaAuthenticator.Authenticator": {
        "type": "object",
        "properties": {
          "okta_id": {
            "type": "string",
            "nullable": true
          },
          "type": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.MfaAuthenticator.MfaAuthenticatorType"
          },
          "enrolled": {
            "type": "boolean"
          },
          "multiple_factors_supported": {
            "type": "boolean"
          },
          "factor_id": {
            "type": "string",
            "nullable": true
          },
          "factors": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Mfa.MfaAuthenticator.Factor"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Mfa.MfaAuthenticator.Factor": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "nullable": true
          },
          "name": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Mfa.MfaAuthenticator.MfaAuthenticatorType": {
        "enum": [
          "unknown",
          "otp",
          "webauthn"
        ],
        "type": "string"
      },
      "UserManagement.WebApi.Mfa.TempMfaEnforcement.MfaEnforcementRequest": {
        "type": "object",
        "properties": {
          "client_id": {
            "type": "string",
            "nullable": true
          },
          "is_force_run": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Models.Requests.CreateUserRequestV2": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Services.GetUser.Models.OktaUser": {
        "type": "object",
        "properties": {
          "okta_user_id": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.OktaUserId"
          },
          "first_name": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.FirstName"
          },
          "last_name": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.LastName"
          },
          "email": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.Email"
          },
          "status": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.UserStatus"
          },
          "is_federated": {
            "type": "boolean"
          },
          "is_internal": {
            "type": "boolean"
          },
          "created": {
            "$ref": "#/components/schemas/Optional.Option`1[System.DateTimeOffset]"
          },
          "updated": {
            "$ref": "#/components/schemas/Optional.Option`1[System.DateTimeOffset]"
          },
          "last_login": {
            "$ref": "#/components/schemas/Optional.Option`1[System.DateTimeOffset]"
          }
        },
        "additionalProperties": false
      },
      "UserManagement.WebApi.Services.Members.Models.Member": {
        "type": "object",
        "properties": {
          "user_id": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.UserId"
          },
          "client_id": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Domain.CkoClientId"
          },
          "roles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/UserManagement.WebApi.Domain.Role"
            },
            "nullable": true
          },
          "entity_segments": {
            "$ref": "#/components/schemas/UserManagement.OktaInlineHook.Domain.Segments.EntitySegments"
          },
          "created": {
            "type": "string",
            "format": "date-time"
          },
          "updated": {
            "$ref": "#/components/schemas/Optional.Option`1[System.DateTime]"
          },
          "okta_user": {
            "$ref": "#/components/schemas/UserManagement.WebApi.Services.GetUser.Models.OktaUser"
          }
        },
        "additionalProperties": false
      }
    },
    "securitySchemes": {
      "Bearer": {
        "type": "http",
        "description": "Put **_ONLY_** your JWT Bearer token on textbox below!",
        "scheme": "Bearer",
        "bearerFormat": "JWT"
      },
      "ApiKeyAuth": {
        "type": "apiKey",
        "description": "Input apikey to access this API",
        "name": "Authorization",
        "in": "header"
      }
    }
  },
  "tags": [
    {
      "name": "Fragments",
      "description": "Public endpoints for user role-related information."
    },
    {
      "name": "Roles",
      "description": "Public endpoints for user role-related information."
    },
    {
      "name": "UserOnboarding",
      "description": "User onboarding Api.\r\nProvides actions for user onboarding and activation."
    },
    {
      "name": "CustomRoles",
      "description": "Management of custom user roles for a Dashboard client."
    },
    {
      "name": "Members",
      "description": "Membership management for external applications (e.g. Dashboard)."
    },
    {
      "name": "Users",
      "description": "User management for external applications (e.g. Dashboard)."
    },
    {
      "name": "AuditLogHook",
      "description": "Okta Event Hook endpoints for creation of audit logs."
    },
    {
      "name": "UpdateMfaEnrollmentHook",
      "description": "Endpoints to update MFA enrollment status based on Okta Event hook, when MFA enrolment is optional."
    },
    {
      "name": "ClientSSOConfiguration",
      "description": "API supporting SSO configuration management."
    },
    {
      "name": "ActivateUser",
      "description": "User onboarding Api.\r\nProvides actions for merchants onboarding and activation."
    },
    {
      "name": "MigrateOktaUserId",
      "description": "Temporary controller for okta user id migration"
    }
  ]
}