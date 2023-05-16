import itertools
import types
import weakref

import pydantic
from fastapi import FastAPI

app = FastAPI()

# CommaSeparatedList parser taken from
# https://github.com/tiangolo/fastapi/issues/50#issuecomment-1267068112


class TypeParametersMemoizer(type):
    _generics_cache = weakref.WeakValueDictionary()

    def __getitem__(self, type_params):
        # prevent duplication of generic types
        if type_params in self._generics_cache:
            return self._generics_cache[type_params]

        # middleware class for holding type parameters
        class TypeParamsWrapper(self):
            __type_parameters__ = (
                type_params if isinstance(type_params, tuple) else (type_params,)
            )

            @classmethod
            def _get_type_parameters(cls):
                return cls.__type_parameters__

        return types.GenericAlias(TypeParamsWrapper, type_params)


class CommaSeparatedList(list, metaclass=TypeParametersMemoizer):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str | list[str]):
        if isinstance(v, str):
            v = v.split(",")
        else:
            v = list(itertools.chain.from_iterable((x.split(",") for x in v)))
        params = cls._get_type_parameters()
        return pydantic.parse_obj_as(list[params], list(map(str.strip, v)))

    @classmethod
    def _get_type_parameters(cls):
        raise NotImplementedError("should be overridden in metaclass")


from .endpoints import *  # noqa: E402, F401, F403
