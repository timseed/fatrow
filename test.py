import logging.config
import logging
import yaml
from fatrow import fatrow

if __name__ == "__main__":
    with open('logging.yaml','rt') as f:
            config=yaml.safe_load(f.read())
            f.close()
    logging.config.dictConfig(config)
    logger=logging.getLogger(__name__)
    logger.debug("main is starting")
    fr = fatrow()
    fr.process('1,this')
    fr.process('1,test')
    fr.process('1,record')
    fr.process('2,junk')
    fr.process('1,a')
    fr.process('3,still')
    fr.process('2,record')
    fr.process('5,end')
    fr.process('1,is')
    fr.process('1,this')
    fr.process('1,test')
    fr.process('1,record')
    fr.process('2,junk')
    fr.process('1,a')
    fr.process('1,this')
    fr.process('1,test')
    fr.process('1,record')
    fr.process('2,junk')
    fr.process('1,a')
    fr.process('3,still')
    fr.process('2,record')
    fr.process('5,end')
    fr.process('1,is')
    fr.process('1,this')
    fr.process('1,test')
    fr.process('1,record')
    fr.process('2,junk')
    fr.process('1,a')
    for k, v in fr:
        logger.debug('' + k + '--->' + str(v))
