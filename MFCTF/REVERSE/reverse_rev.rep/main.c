
undefined8 main(int param_1,uchar *param_2,size_t param_3,uchar *param_4,size_t param_5)

{
  int iVar1;
  undefined8 uVar2;
  
  if (param_1 < 2) {
    fwrite("I need a key!\n",1,0xe,stderr);
    uVar2 = 0xffffffff;
  }
  else {
    iVar1 = verify(*(EVP_PKEY_CTX **)(param_2 + 8),param_2,param_3,param_4,param_5);
    if (iVar1 == 0) {
      puts("Wrong key!");
    }
    else {
      puts("Correct key!");
    }
    uVar2 = 0;
  }
  return uVar2;
}

