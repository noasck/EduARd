## Deployment

#### Useful aliases
``` bash
alias dc_build_dev='docker-compose -f docker-compose.yml up --build'
alias dc_build_test='docker-compose -f docker-compose.test.yml up --build'
alias dc_build_prod='docker-compose -f docker-compose.prod.yml up --build'

alias dc_down_dev='docker-compose -f docker-compose.yml down --volumes --remove-orphans'
alias dc_down_test='docker-compose -f docker-compose.test.yml down --volumes --remove-orphans'
alias dc_down_prod='docker-compose -f docker-compose.prod.yml down --volumes --remove-orphans'
```
**Optionally:** you could add ```-d``` key after alias-called script to *run docker services in the background*. 
(E.g. ```dc_build_prod -d```)
### Testing
- Up: ```dc_build_test```
- Down: ```dc_down_test```
### Development
- Up: ```dc_build_dev```
- Down: ```dc_down_dev```
### Production
- Up: ```dc_build_prod```
- Down: ```dc_down_prod```
