from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://hed1x7hh71r7dhy9uvx1:pscale_pw_esfRX4BP3CCPuMOM53qe3RYzhQ2qo0x0mM9O3m9uJy2@aws.connect.psdb.cloud/researchcareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
      "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
      }
  })


with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(row._mapping)

  print(result_dicts)
 
