class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file):
        props = {}
        with open(property_file, 'r') as file:
            for line in file:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    props[key] = value
        conn_str = (
            f"DRIVER={{{props['DB_DRIVER']}}};"
            f"SERVER={props['DB_SERVER']};"
            f"DATABASE={props['DB_NAME']};"
            f"UID={props['DB_USER']};"
            f"PWD={props['DB_PASSWORD']}"
        )
        return conn_str
