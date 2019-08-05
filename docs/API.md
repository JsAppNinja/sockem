# Authorization 
## Obtaining tokens
* Make a POST request to `/api/api-token-auth/` with valid `username` and `password` fields to receive a users token key
* Example:

```
{
    "username": "admin",
    "password": "password"
}
```

## Making requests with tokens
* In the HTTP request header, include the token key in this form (note the whitespace after 'Token')

`Authorization: Token be1314c3be8264b2f3b1a46de5fb9e05ef4e9808`

# POST /api/users/
* The JSON body should match the form below. Password is 78 chars long is hashed using Django's default PBKDF2 algorithm.
```
{
    "email": "admin@sockemboppem.com",
    "username": "admin",
    "password": "unhashedpassword",
    "avatar": someurlhere
}
```

# POST /api/tournaments/
* The JSON body should match the form below, with `is_judge` indicating whether the tournament creator wishes to join
  as a judge.
  
* The `creator` field is missing from the request and filled out automatically based on the user tied to the 
  authorization token
```
{
	"name": "Biggest's Pasta Tournament",
	"start_date": "2019-07-29 21:51:23+00",
	"users": [
		{
            "is_judge": false
        }
    ]
}
```

# POST /api/tournament_users/
* The JSON body should match the form below, with `is_judge` indicating whether the user is a judge in this tournament
* The `user` field is missing from the request and filled out automatically based on the user tied to the 
  authorization token
* For the `tournament` field, send the URL instead of the raw primary key
```
{
    "tournament": "http://localhost:8000/api/tournaments/1",
    "is_judge": true
}
```

# POST /api/matches/
* The JSON body should match the form below. `round` need to be `>= 1`
* For the `tournament` field, send the URL instead of the raw primary key
* Matches form a tree structure and via the `prev_matches` field.
* The highest round number match should be at the root
* `prev_matches` can be omitted from POST requests for leaf matches

```
{
    "tournament": "http://localhost:8000/api/tournaments/1", 
    "round": 4,
    "prev_matches": [
    	"http://localhost:8000/api/matches/12", 
    	"http://localhost:8000/api/matches/7"
	]
}
```

# POST /api/match_users/
* The JSON body should match the form below. 
* For the `user` and `match` fields, send the URLs instead of the raw primary keys
```
{
    "user": "http://localhost:8000/api/users/5",
    "match": "http://localhost:8000/api/matches/2"
}
```

# POST /api/games/
* The JSON body should match the form below.
* For the `match` and `winner` fields, send the URLs instead of the raw primary keys
```
{
    "match": "http://localhost:8000/api/matches/2",
    "winner": "http://localhost:8000/api/users/5",
    "start_time": "2019-07-30T20:56:49Z",
    "end_time": "2019-07-30T20:56:51Z"
}
```
