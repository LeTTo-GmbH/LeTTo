# Setup Environment
siehe auch
* [docker compose files](/notimplemented/index.md)
* [Administration](../Administration/index.md)

###  Setup Environment 

| Variable                                         | Beschreibung                                                                 | mögliche/default Werte          |
|--------------------------------------------------|------------------------------------------------------------------------------|---------------------------------|
| LETTO_UID                                        |                                                                              |                                 |
| RUN_AS_ROOT                                      |                                                                              | true                            |
| LETTO_RESTKEY                                    |                                                                              |                                 |
| SERVICE_USER_PASSWORD                            |                                                                              |                                 |
| SERVICE_GAST_PASSWORD                            |                                                                              |                                 |
| SERVICE_ADMIN_PASSWORD                           |                                                                              |                                 |
| LETTO_PATH                                       |                                                                              | /opt/letto                      |
| SETUP_COMPOSE                                    |                                                                              | /opt/letto/docker/compose/setup |
| LETTO_COMPOSE                                    |                                                                              | /opt/letto/docker/compose/letto |
| HOST_BS                                          |                                                                              | LINUX                           |
| PATH_SEPERATOR                                   |                                                                              | /                               |
| STABLE                                           |                                                                              | false                           |
| DEBUG                                            |                                                                              | false                           |
| SETUP_MAIN                                       |                                                                              | AUTO                            |
| JWT_SECRET                                       |                                                                              |                                 |
| SERVER_SECRET                                    |                                                                              |                                 |
| LETTO_LOCAL_PRIVATE_KEY                          |                                                                              |                                 |
| LETTO_LOCAL_PUBLIC_KEY                           |                                                                              |                                 |
| ADMIN_LOGFILE_WITH_DOCKER                        |                                                                              | false                           |                 
| WATCHDOG                                         |                                                                              | ON                              |                                     
| WATCHDOG_MAX_CPU                                 |                                                                              | 400                             |                            
| WATCHDOG_MAX_TIME                                |                                                                              | 130                             |                           
| ADMIN_PASSWORD                                   |                                                                              |                                 |
| HTTPS_PORT                                       |                                                                              | 3096                            |                               
| ADMIN_PASSWORD_ENCRYPTED                         |                                                                              |                                 |
| LOCAL_BACKUP                                     |                                                                              | false                           |
| TIME_DAILY_BACKUP                                |                                                                              | 0:30                            |
| BACKUP_STOP_LETTO                                |                                                                              | true                            |
| BACKUP_MIN_FREE_DISK_SPACE_MB                    |                                                                              | 20000                           |
| BACKUP_DATABASE                                  |                                                                              | true                            |
| BACKUP_DATABASE_DAY_OF_WEEK                      |                                                                              | true                            |
| BACKUP_DATABASE_MONTHLY_IMAGE                    |                                                                              | true                            |
| BACKUP_IMAGE                                     |                                                                              | false                           |
| BACKUP_IMAGE_DAY_OF_WEEK                         |                                                                              | false                           |
| BACKUP_IMAGE_MONTHLY_IMAGE                       |                                                                              | false                           |
| BACKUP_PROJEKTE                                  |                                                                              | false                           |
| BACKUP_PROJEKTE_DAY_OF_WEEK                      |                                                                              | false                           |
| BACKUP_PROJEKTE_MONTHLY_IMAGE                    |                                                                              | false                           |
| REFRESH_LETS_ENCRYPT_AUTO                        |                                                                              | true                            |
| CHECK_LICENSE_AUTO                               |                                                                              | true                            |
| SETUP_UPDATE                                     |                                                                              | stable                          |
| spring_mail_host                                 |                                                                              |                                 |
| spring_mail_port                                 |                                                                              | 465                             |
| spring_mail_username                             |                                                                              | office@letto.at                 |
| spring_mail_password                             |                                                                              |                                 |
| spring_mail_properties_mail_smtp_auth            |                                                                              | true                            |
| spring_mail_properties_mail_smtp_starttls_enable |                                                                              | true                            |
| spring_mail_properties_mail_smtp_ssl_enable      |                                                                              | true                            |
| spring_mail_address_noreply                      |                                                                              | noreply@letto.at                |
| spring_mail_address_reply                        |                                                                              | service@letto.at                |
| ADDITIONAL_DATABASES                             | Liste aller Datenbanken die zusätzlich ins Datenbankbackup integriert werden |                                 |
