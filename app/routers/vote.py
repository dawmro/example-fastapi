from ctypes.wintypes import HACCEL
from logging import raiseExceptions
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2


router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code = status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    # checking if voting on post that does not exist
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id: {vote.post_id} does not exist")

    # checking if vote exists and if belongs to current user
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)

    # saving first result of query
    found_vote = vote_query.first()

    # add vote direction
    if(vote.dir == 1):
        # if user already added vote don't allow him to add vote again
        if found_vote:
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail =f"user {current_user.id} already voted on post {vote.post_id}")

        # if vote not found create new vote
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}

        
    # remove vote direction
    else:
        # don't remove vote if does not exist
        if not found_vote:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =f"Vote does not exist")

        # delete vote
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "succesfully deleted vote"}


