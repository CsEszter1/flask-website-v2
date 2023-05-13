from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://4houhauooj3mrcavvnns:pscale_pw_zmbz5SPm9LRi8cHBQA8pgzOj4KxmZmmpUZZkuyzq93U@aws.connect.psdb.cloud/researchcareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
      "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
      }
  })



def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
  return jobs
