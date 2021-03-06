import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from github_searcher.models import Base, engine, Repo
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    for repo in session.query(Repo).all():
        print("%s - %d stars, lang:%s" % (repo.name, repo.total_stars, repo.language))
        for issue in repo.issues:
            print(
                "\t[%s]\t%s with %d comments, created at %s | ID = %d | REPO ID = %d"
                % (
                    issue.category,
                    issue.title,
                    issue.total_comments,
                    issue.created_at,
                    issue.issue_id,
                    issue.repo_id,
                )
            )
        print()
