import base64, base45, binascii, zlib, sys

s = ("06GS6YE3MJB00TTJKEZWGIQKGFFECNMOWQQYRYVGTGFSMPARHQRVPHAXBNITVHRTWZAFWAJOQJUNBAETQERFEFAUBIJZNCIGNSKRHOQEYQEPCOAYRADWXZPYUKPWARSTBMKQCOIJXHVMXDBKBSREUZHWNKEHSLCVFDNOJUBFEWHNKKTFCTNDPYBBPOSTFOUQLPZCMEVAATFSAXUZWBTFELDSFDJSGSIOYCLBUPKGI")

def try_print(label, b: bytes):
    # Show a quick preview
    asciiish = all(32 <= c <= 126 or c in (9,10,13) for c in b)
    preview = b[:64]
    print(f"[{label}] {len(b)} bytes; asciiish={asciiish}; preview={preview!r}")
    # Try zlib/gzip
    for comp in ("zlib", "gzip"):
        try:
            if comp == "zlib":
                d = zlib.decompress(b)
            else:
                import gzip, io
                d = gzip.decompress(b)
            print(f"  -> {comp} decompress OK ({len(d)} bytes), preview={d[:64]!r}")
        except Exception:
            pass

# 1) Base45
try:
    import base45
    b = base45.b45decode(s)
    try_print("base45", b)
except Exception as e:
    print("[base45] no:", e)

# 2) Base32 (casefold) — unlikely because of digits 0/1/8/9 but try
try:
    b = base64.b32decode(s, casefold=True)
    try_print("base32", b)
except Exception as e:
    print("[base32] no:", e)

# 3) Base64 (standard and urlsafe) — unlikely (no + / =)
for label, func in (("base64", base64.b64decode), ("base64_urlsafe", base64.urlsafe_b64decode)):
    t = s + "==="  # pad just in case
    try:
        b = func(t)
        try_print(label, b)
    except Exception as e:
        print(f"[{label}] no:", e)

# 4) Base36 → int → bytes
try:
    n = int(s, 36)
    # convert big int to minimal bytes
    blen = (n.bit_length() + 7) // 8
    b = n.to_bytes(blen, "big")
    try_print("base36->bytes", b)
except Exception as e:
    print("[base36] no:", e)



# I believe the string is encrypted with a key at the backend.