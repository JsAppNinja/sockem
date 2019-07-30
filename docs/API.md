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

# POST /api/tournaments/
* The JSON body should match the form below, with `is_judge` indicating whether the tournament creator wishes to join
  as a judge.
```
{
	"name": "Biggest Pasta Tournament",
	"start_date": "2019-07-29 21:51:23+00",
	"creator": 2,
	"users":
		[{
            "is_judge": false
        }]
}
```

# POST /api/matches/
* The JSON body should match the form below. `round` and `num_games` both need to be `>= 1`

```
{
    "tournament": 1, 
    "round": 1,
    "num_games": 3
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

