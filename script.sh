stages:
    - upload

variables:
  VAULT_ADDR:
      description: "Пропиши путь куда сложить секреты"

Upload_Secret:
    stage: upload
    before_script:
        -  chmod +x script.sh
    script:
        - ./script.sh $VAULT_ADDR
    only:
        - master
