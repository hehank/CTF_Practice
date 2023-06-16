
int verify(EVP_PKEY_CTX *ctx,uchar *sig,size_t siglen,uchar *tbs,size_t tbslen)

{
  uint local_c;
  
  local_c = 0;
  while( true ) {
    if (ctx[(int)local_c] == (EVP_PKEY_CTX)0x0) {
      return (uint)(local_c == 0x22);
    }
    if (encrypted[(int)local_c] !=
        (byte)(((byte)((int)((byte)ctx[(int)local_c] ^ local_c) >>
                      (8 - (((byte)local_c ^ 9) & 3) & 0x1f)) |
               (byte)(((byte)ctx[(int)local_c] ^ local_c) << (((byte)local_c ^ 9) & 3))) + 8))
    break;
    local_c = local_c + 1;
  }
  return 0;
}

