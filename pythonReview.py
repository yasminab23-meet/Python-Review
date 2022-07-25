input =("Title:")
input =("Description:")


def create_youtube_video (title,desc):
	youtube_dict= {"Title":title, "Description":desc, "Likes":0,"Dislikes":0, "Comments":{} }
	return youtube_dict 


def like (youtube_dict):

	if "Likes" in youtube_dict:
		youtube_dict["Likes"] += 1
	return youtube_dict 

def dislike (youtube_dict):

	if "Dislike" in youtube_dict:
		youtube_dict["Dislikes"] +=1
	return youtube_dict

def add_comment (youtube_dict,username,comment_text):
	youtubevideo = {}

	Comments["Username"]= comment_text

	return youtube_dict


