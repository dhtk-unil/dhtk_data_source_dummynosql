"""
This module is a minimal example for DHTK data sources using Mongo database.

This module should live in the namespace: dhtk.data_sources.[NAME_OF_THE_DATA_SOURCE]



Notes:

In this case we use dhtk_storage_docker as the provider for the Mongo database.

$ pip install dhtk_storage_docker

Example:

>>> import dhtk
>>> d = dhtk.start("../WD", data_source="dummymongo", storage="docker")
"""
import warnings
import re
import logging

import pymongo
from dhtk.data_sources.blueprint import AbstractDataSource

logger = logging.getLogger(__name__)

warnings.formatwarning = lambda message, *args: f"{message}\n"


class Module(AbstractDataSource):
    """
    This class exemplifies a DHTK datasource using an Mongo Database.

    Notes:
        Always name the class "Module" and always inherit from AbstactDataSource
        The class attibutes: "name" "storage_type" "data_file" and the class method "get_data_file"
        and the "get" method have to be defined.
        The attribute "name" has to be the same as NAME_OF_THE_DATA_SOURCE.
        The class method "get_data_file"  method should always accept the arguments:
        The __init__ method should always accept the arguments: working_directory and endpoints.
    """
    name = "dummymongo"
    storage_type = "nosql"
    data_file = """
    DROP DATABASE IF EXISTS dhtk;
    CREATE DATABASE IF NOT EXISTS dhtk;
    USE dhtk;

    CREATE OR REPLACE TABLE test (id INT NOT NULL, name CHAR(10));
    
    INSERT INTO `test` VALUES (1001, 'Mattia'), (1002, 'Davide');
    """.replace(r"\t", "")

    @classmethod
    def get_data_file(cls, output_path, storage_type):
        """Put the datafile to the output path.

        In this case we write the data_file specified as string in the class attribute "data_file"
        to the output_path.

        Notes:
            the file should be an sql dump.
            This dump will be loaded onto the database by the storage module.

        Args:
            output_path:
                the path where the file should be put.
            storage_type:
                only useful if there are multiple storage types and thus data files.
                In this case ignore it.
        Returns
            a pathlib.Path to the written file.
        """
        dumpfile = output_path / "dump.sql"
        with dumpfile.open("w", encoding="utf-8") as out_file:
            out_file.write(cls.data_file)
        return dumpfile

    def __init__(self, working_directory, endpoints):
        """
        Initialise the Module.

        In this case we test if the storage module has loaded the data.

        Args:
            working_directory:
                will recive the dhtk working directory.
            endpoints:
                a list of endpointd provided by the storage module.
        """
        endpoint = endpoints[0]
        getinfo = re.compile(r".*\/\/(.*?):(\d+)$")
        matches = getinfo.match(endpoint)
        engine = sqlalchemy.create_engine(f"mariadb+pymysql://{matches.group(1)}")
        client = pymongo.MongoClient("matches.group(1)", int(matches.group(2)))

    def get(self, what, name="all", add=False):
        """Get the data.

        Notes:
            It is not implemented as this is only a dummy module. But it should be the main
            interface for the user to use your data_source.
        """
        return "OK"
