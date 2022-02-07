# Flask-Terc
Terc-import

Task 3 solution: https://stackoverflow.com/questions/54433522/docker-compose-and-postgres-name-does-not-resolve
other one to try: https://stackoverflow.com/questions/66581899/docker-python-database-could-not-translate-host-name

Network of containers inspect result:
```
[
    {
        "Name": "flaskterc_default",
        "Id": "51d191c617375e40a3412c32016e78f635b22650e2a3eaf478ece076858e79c7",
        "Created": "2022-02-07T16:16:23.121126812+01:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": true,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "81f12309e9b65d6ee03af57415a4a6ba3faf03c25a95da22ded208d67bcd7f1b": {
                "Name": "postgres",
                "EndpointID": "2f35de4c7fcc879931ca210452b669d8116d51f3fa6d907a7097630c1a6c206a",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {
            "com.docker.compose.network": "default",
            "com.docker.compose.project": "flaskterc"
        }
    }
]

```


Postgres container log:


```
sudo docker logs 81f12309e9b6

PostgreSQL Database directory appears to contain a database; Skipping initialization

2022-02-07 16:33:45.385 UTC [1] LOG:  starting PostgreSQL 14.1 (Debian 14.1-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
2022-02-07 16:33:45.386 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2022-02-07 16:33:45.386 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2022-02-07 16:33:45.422 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2022-02-07 16:33:45.438 UTC [26] LOG:  database system was shut down at 2022-02-07 16:33:43 UTC
2022-02-07 16:33:45.448 UTC [1] LOG:  database system is ready to accept connections
```


