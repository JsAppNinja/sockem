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
    "password": "pbkdf2_sha256$150000$529zbhCR1s71$uViN4aYhKfel/1Rpk9LtknaG1bW9uxDK2kfwvXHaa+Y=",
    "avatar": someurlhere
}
```

# POST /api/tournaments/
* The JSON body should match the form below, with `is_judge` indicating whether the tournament creator wishes to join
  as a judge.
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
```
{
    "user": 2,
    "tournament": 2,
    "is_judge": true
}
```

# POST /api/matches/
* The JSON body should match the form below. `round` and `num_games` both need to be `>= 1`

```
{
    "tournament": 1, 
    "round": 1
}
```

# POST /api/match_users/
* The JSON body should match the form below. 

```
{
    "user": 1,
    "match": 1
}
```

# POST /api/games/
* The JSON body should match the form below.
```
{
    "match": 1,
    "winner": 3,
    "start_time": "2019-07-30T20:56:49Z",
    "end_time": "2019-07-30T20:56:51Z"
}
```
