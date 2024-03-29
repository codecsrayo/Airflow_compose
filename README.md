# Airflow_compose
Apache Airflow es una plataforma de gestión de flujo de trabajo de código abierto escrita en Python, donde los flujos de trabajo se crean a través de scripts de Python

# test
```bash
    airflow tasks run <DAG_ID> <TASK_ID> <EXECUTION_DATE_OR_RUN_ID>
```


Miscellaneous commands                                                                               
airflow cheat-sheet                       | Display cheat sheet                                      
airflow dag-processor                     | Start a standalone Dag Processor instance                
airflow info                              | Show information about current Airflow and environment   
airflow kerberos                          | Start a kerberos ticket renewer                          
airflow plugins                           | Dump information about loaded plugins                    
airflow rotate-fernet-key                 | Rotate encrypted connection credentials and variables    
airflow scheduler                         | Start a scheduler instance                               
airflow standalone                        | Run an all-in-one copy of Airflow                        
airflow sync-perm                         | Update permissions for existing roles and optionally DAGs
airflow triggerer                         | Start a triggerer instance                               
airflow version                           | Show the version                                         
airflow webserver                         | Start a Airflow webserver instance                       
                                                                                                     
Celery components                                                            
airflow celery flower                     | Start a Celery Flower            
airflow celery stop                       | Stop the Celery worker gracefully
airflow celery worker                     | Start a Celery worker node       
                                                                             
View configuration                                                              
airflow config get-value                  | Print the value of the configuration
airflow config list                       | List options for the configuration  
                                                                                
Manage connections                                                        
airflow connections add                   | Add a connection              
airflow connections delete                | Delete a connection           
airflow connections export                | Export all connections        
airflow connections get                   | Get a connection              
airflow connections import                | Import connections from a file
airflow connections list                  | List connections              
                                                                          
Manage DAGs                                                                                    
airflow dags backfill                     | Run subsections of a DAG for a specified date range
airflow dags delete                       | Delete all DB records related to the specified DAG 
airflow dags list                         | List all the DAGs                                  
airflow dags list-import-errors           | List all the DAGs that have import errors          
airflow dags list-jobs                    | List the jobs                                      
airflow dags list-runs                    | List DAG runs given a DAG id                       
airflow dags next-execution               | Get the next execution datetimes of a DAG          
airflow dags pause                        | Pause a DAG                                        
airflow dags report                       | Show DagBag loading report                         
airflow dags reserialize                  | Reserialize all DAGs by parsing the DagBag files   
airflow dags show                         | Displays DAG's tasks with their dependencies       
airflow dags show-dependencies            | Displays DAGs with their dependencies              
airflow dags state                        | Get the status of a dag run                        
airflow dags test                         | Execute one single DagRun                          
airflow dags trigger                      | Trigger a DAG run                                  
airflow dags unpause                      | Resume a paused DAG                                
                                                                                               
Database operations                                                                        
airflow db check                          | Check if the database can be reached           
airflow db check-migrations               | Check if migration have finished               
airflow db clean                          | Purge old records in metastore tables          
airflow db downgrade                      | Downgrade the schema of the metadata database. 
airflow db init                           | Initialize the metadata database               
airflow db reset                          | Burn down and rebuild the metadata database    
airflow db shell                          | Runs a shell to access the database            
airflow db upgrade                        | Upgrade the metadata database to latest version
                                                                                           
Manage jobs                                                                 
airflow jobs check                        | Checks if job(s) are still alive
                                                                            
Tools to help run the KubernetesExecutor                                                                                                                             
airflow kubernetes cleanup-pods           | Clean up Kubernetes pods (created by KubernetesExecutor/KubernetesPodOperator) in evicted/failed/succeeded/pending states
airflow kubernetes generate-dag-yaml      | Generate YAML files for all tasks in DAG. Useful for debugging tasks without launching into a cluster                    
                                                                                                                                                                     
Manage pools                                                
airflow pools delete                      | Delete pool     
airflow pools export                      | Export all pools
airflow pools get                         | Get pool size   
airflow pools import                      | Import pools    
airflow pools list                        | List pools      
airflow pools set                         | Configure pool  
                                                            
Display providers                                                                                                   
airflow providers auth                    | Get information about API auth backends provided                        
airflow providers behaviours              | Get information about registered connection types with custom behaviours
airflow providers get                     | Get detailed information about a provider                               
airflow providers hooks                   | List registered provider hooks                                          
airflow providers links                   | List extra links registered by the providers                            
airflow providers list                    | List installed providers                                                
airflow providers logging                 | Get information about task logging handlers provided                    
airflow providers secrets                 | Get information about secrets backends provided                         
airflow providers widgets                 | Get information about registered connection form widgets                
                                                                                                                    
Manage roles                                                                                       
airflow roles add-perms                   | Add roles permissions                                  
airflow roles create                      | Create role                                            
airflow roles del-perms                   | Delete roles permissions                               
airflow roles delete                      | Delete role                                            
airflow roles export                      | Export roles (without permissions) from db to JSON file
airflow roles import                      | Import roles (without permissions) from JSON file to db
airflow roles list                        | List roles                                             
                                                                                                   
Manage tasks                                                                                  
airflow tasks clear                       | Clear a set of task instance, as if they never ran
airflow tasks failed-deps                 | Returns the unmet dependencies for a task instance
airflow tasks list                        | List the tasks within a DAG                       
airflow tasks render                      | Render a task instance's template(s)              
airflow tasks run                         | Run a single task instance                        
airflow tasks state                       | Get the status of a task instance                 
airflow tasks states-for-dag-run          | Get the status of all task instances in a dag run 
airflow tasks test                        | Test a task instance                              
                                                                                              
Manage users                                                       
airflow users add-role                    | Add role to a user     
airflow users create                      | Create a user          
airflow users delete                      | Delete a user          
airflow users export                      | Export all users       
airflow users import                      | Import users           
airflow users list                        | List users             
airflow users remove-role                 | Remove role from a user
                                                                   
Manage variables                                                
airflow variables delete                  | Delete variable     
airflow variables export                  | Export all variables
airflow variables get                     | Get variable        
airflow variables import                  | Import variables    
airflow variables list                    | List variables      
airflow variables set                     | Set variable


# Windows: Habilitar el servidor ssh
______________________________________
Windows PowerShell
Copyright (C) Microsoft Corporation. Todos los derechos reservados.
                                                                                                                        Prueba la nueva tecnología PowerShell multiplataforma https://aka.ms/pscore6                                                                                                                                                                    PS C:\WINDOWS\system32> Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0                                   

Path          :
Online        : True
RestartNeeded : False



PS C:\WINDOWS\system32> Set-Service -Name ssh-agent -StartupType 'Automatic'
PS C:\WINDOWS\system32> Set-Service -Name sshd -StartupType 'Automatic'
PS C:\WINDOWS\system32> Get-Service ssh*

Status   Name               DisplayName
------   ----               -----------
Stopped  ssh-agent          OpenSSH Authentication Agent
Stopped  sshd               OpenSSH SSH Server


PS C:\WINDOWS\system32> Get-Service ssh* | Start-Service

######################
##### .env Example
#######################

# Meta-Database
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow

# Airflow Core
AIRFLOW__CORE__FERNET_KEY=UKMzEm3yIuFYEq1y3-2FxPNWSVwRASpahmQ9kQfEr8E=
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=True
AIRFLOW__CORE__LOAD_EXAMPLES=False
AIRFLOW_UID=0

# Backend DB
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
AIRFLOW__DATABASE__LOAD_DEFAULT_CONNECTIONS=False

# Airflow Init
_AIRFLOW_DB_UPGRADE=True
_AIRFLOW_WWW_USER_CREATE=True
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow

PGADMIN_DEFAULT_EMAIL=example@example.com
PGADMIN_DEFAULT_PASSWORD=12345


#Al habilitar esta variable, se utilizará la sintaxis extendida del archivo Dockerfile y el motor de construcción de #imágenes de BuildKit en lugar del motor de construcción de imágenes antiguo de Docker. Esto puede mejorar la #velocidad y eficiencia de la construcción de imágenes de Docker, especialmente para imágenes más grandes y complejas

DOCKER_BUILDKIT=1