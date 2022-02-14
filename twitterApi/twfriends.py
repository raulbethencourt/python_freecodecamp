import urllib.request
import urllib.parse
import urllib.error
import json
import sqlite3
import twurl
import ssl

TWITTER_URL = "https://api.twitter.com/1.1/friends/list.json"

conn = sqlite3.connect("friends.sqlite")
cur = conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS People(id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)"
)
cur.execute(
    "CREATE TABLE IF NOT EXISTS Follows(from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))"
)

# Ingore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input("Enter a Twitter account, or quit: ")
    if acct == "quit":
        break
    if len(acct) < 1:
        cur.execute("SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1")
        try:
            (id, acct) = cur.fetchone()
        except:
            print("No unretrieved Twitter accounts found")
            continue
    else:
        cur.execute("SELECT id FROM People WHERE name = ? LIMIT 1", (acct,))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute(
                "INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)", (acct,)
            )
            conn.commit()
            if cur.rowcount != 1:
                print("Error insterting account:", acct)
                continue
            id = cur.lastrowid

    url = twurl.augment(TWITTER_URL, {"screen_name": acct, "count": "100"})
    print("Retrieving account", acct)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print("Remaining", headers["x-rate-limit-remaining"])

    try:
        js = json.loads(data)
    except:
        print("Unable to parse json")
        print(data)
        break

    if "users" not in js:
        print("Incorrect json received")
        print(json.dumps(js, indent=4))
        continue

    cur.execute("UPDATE Peaople SET retrieved=1 WHERE name=?", (acct,))

    countnew = 0
    countold = 0
    for u in js["users"]:
        friend = u["screen_name"]
        print(friend)
        cur.execute("SELECT id FROM Peaople WHERE name=? LIMIT 1", (friend,))
        try:
            frined_id = cur.fetchone()[0]
            countold = countnew + 1
        except:
            cur.execute(
                "INSERT OR IGNORE INTO Peaople (name, retrieved) VALUES (?, 0)",
                (friend,),
            )
            conn.commit()
            if cur.rowcount != 1:
                print("Error insterting account:", friend)
                continue
            frined_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute(
            "INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?, ?)",
            (id, frined_id),
        )

    print("New accounts=", countnew, "revisited=", countold)
    conn.commit()
cur.close()
