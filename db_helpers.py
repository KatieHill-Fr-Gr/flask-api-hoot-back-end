import os
import psycopg2, psycopg2.extras

def get_db_connection():
    connection = psycopg2.connect(
        host='localhost',
        database=os.getenv('POSTGRES_DATABASE'),
        user=os.getenv('POSTGRES_USERNAME'),
        password=os.getenv('POSTGRES_PASSWORD')
    )   
    return connection

def consolidate_comments_in_hoots(hoots_with_comments):
    print(hoots_with_comments)

    # creates a new list of consolidated_hoots (with the comments)
    consolidated_hoots = []
    for hoot in hoots_with_comments:
        hoot_exists = False
        # searches for the hoot in the consolidated hoots list
        for consolidated_hoot in consolidated_hoots:
            if hoot['id'] == consolidated_hoot['id']:
                # if it finds it hoot_exists is set to True
                hoot_exists = True
                # comment is then appended to the hoot comments list
                consolidated_hoot['comments'].append(
                    {'comment_text': hoot['comment_text'],
                     'comment_id': hoot['comment_id'],
                      'comment_author_username': hoot['comment_author_username']
                      })
                break # stops this particular loop because matching hoot is found so no need to keep search

    if not hoot_exists:
        # if the hoot isn't in already, create a new comments list on it
        hoot['comments'] = []
        # if there's a comment linked to the hoot, append it to the list
        if hoot['comment_id'] is not None:
            hoot['comments'].append(
                {'comment_text': hoot['comment_text'],
                 'comment_id': hoot['comment_id'],
                 'comment_author_username': hoot['comment_author_username']
                 }
            )
        # cleans up the fields that aren't needed at hoot level
        # you're normalising the structure so that the hoot-level data stays at the top and comments data only lives inside hoots['comments']
        del hoot['comment_id']
        del hoot['comment_text']
        del hoot['comment_author_username']
        # finally add the hoot to the consolidated hoots
        consolidated_hoots.append(hoot)
    
    return consolidated_hoots

