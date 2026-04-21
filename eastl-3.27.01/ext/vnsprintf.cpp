//
// Created by Max Godefroy on 21/04/2026.
//

#include <codecvt>
#include <locale>
#include <EASTL/string.h>

namespace EA::StdC
{
    int Vsnprintf(
        char* EA_RESTRICT pDestination,
        const size_t n,
        const char* EA_RESTRICT pFormat,
        const va_list arguments)
    {
        return vsnprintf(pDestination, n, pFormat, arguments);
    }

    int Vsnprintf(
        char16_t* EA_RESTRICT pDestination,
        const size_t n,
        const char16_t* EA_RESTRICT pFormat,
        const va_list arguments)
    {
        std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
        std::string utf8Format = converter.to_bytes(pFormat);

        if (pDestination != nullptr)
        {
            std::string tempBuffer;
            tempBuffer.resize(n);

            const int size = std::vsnprintf(
                tempBuffer.data(),
                n,
                utf8Format.c_str(),
                arguments);

            const std::u16string utf16Result = converter.from_bytes(tempBuffer);
            utf16Result.copy(pDestination, size);
            return size;
        }
        else
        {
            return std::vsnprintf(nullptr, 0, utf8Format.c_str(), arguments);
        }
    }

#if EA_CHAR8_UNIQUE
    int Vsnprintf(
        char8_t* pDestination,
        const size_t n,
        const char8_t*  pFormat,
        const va_list arguments)
    {
        return vsnprintf(reinterpret_cast<char*>(pDestination), n, reinterpret_cast<const char*>(pFormat), arguments);
    }
#endif
}