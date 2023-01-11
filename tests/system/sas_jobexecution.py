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

from datetime import datetime
from airflow import DAG
from sas_airflow_provider.operators.sas_jobexecution import SASJobExecutionOperator

dag = DAG('sas_hello_world_jes', description='Hello World SAS DAG',
          schedule="@once",
          start_date=datetime(2022, 6, 1), catchup=False)


# job parameters are passed into the job
job_parameters = {
    "userName": "Demo"
}

hello_task = SASJobExecutionOperator(task_id='hello_task',
                                     job_name='/Public/Airflow/Hello-World',
                                     parameters=job_parameters,
                                     dag=dag)

if __name__ == '__main__':
    dag.test()