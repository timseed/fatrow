from collections import OrderedDict
import logging.config
import logging
import yaml


class fatrow(object):
    def __init__(self):
        self.ds = {}
        self.logger = logging.getLogger(__name__)
        self.logger.debug(str.format('{} initialized',__name__))


    def process(self, line_of_data, delim=',', key=0):
        '''
        Process a line of data. Adding the unique values to a dictionary.

        Please note: Duplicate values are removed.

        :param line_of_data:
        :param delim: the delimiter of the data
        :param key: key to be extracted, starting at 0. This is removed from the data passed
        :return: Nothing
        '''

        try:
            parts = line_of_data.split(delim)
            try:
                keyvalue = parts[key]
                new_parts = parts[:key] + parts[key + 1:]
                self.logger.debug(str.format('{} {}',keyvalue,str(new_parts)))
                if keyvalue not in self.ds:
                    self.ds[keyvalue] = []
                    for np in new_parts:
                        self.ds[keyvalue].append(np)
                else:
                    try:
                        to_add = list(set(new_parts)-set(self.ds[keyvalue]))
                        self.logger.debug(str.format('Dict{} May_Add{} Diff{}',str(self.ds[keyvalue]),str(new_parts),str(to_add)))
                        if len(to_add)>0:
                            for ta in to_add:
                                self.ds[keyvalue].append(ta)
                    except:
                        self.logger.debug("Finding additions error")
            except IndexError:
                self.logger.debug(str.format("Error getting key {} from {}", key, line_of_data))
                pass
        except:
            self.logger.debug("Split Line Error")
            pass

    def __iter__(self):
        '''
        Simple iterator to allow access to the key Ordered data

        :return: a Tuple (key, list of values)
        '''
        od = OrderedDict(self.ds.items())
        for i in od:
            yield (i, self.ds[i])

