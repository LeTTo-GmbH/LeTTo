# DTOs des Referenz-Plugins (Python)
<!-- erstellt aus plugin-demo-python @ 10ecc4f (revision 1000) – bei Änderungen im Plugin-Repo nachziehen -->

* Die DTOs sind Pydantic-Modelle in `app/main.py` mit **denselben Feldnamen wie die Java-DTOs**; das JSON auf der Leitung ist daher gleich.
  Die Bedeutung jedes Feldes steht in der [DTO-Doku des Java-Plugins](../../referenz-plugin-java/dtos/index.md).
* Alle Modelle verwenden `extra="ignore"`: unbekannte Felder im Request werden ignoriert.
* Enums werden als String übertragen (z.B. `"RELATIV"`, `"OK"`) – das entspricht der JSON-Darstellung der Java-Enums.
  Die erlaubten Werte stehen in den [Enums des Java-Plugins](../../referenz-plugin-java/enums/index.md).
* Java-`long` wird zu `int`, Java-`double` zu `float`, Listen zu `List[...]`, HashMaps zu `Dict[str, ...]`.

## Übersicht

| Python-Modell | Java-Doku | Abweichung |
|---|---|---|
| `AdminInfoDto` | [AdminInfoDto](../../referenz-plugin-java/dtos/AdminInfoDto/index.md) | **andere Felder**, siehe unten |
| `CalcErgebnisDto` | [CalcErgebnisDto](../../referenz-plugin-java/dtos/CalcErgebnisDto/index.md) | Feld heißt in Python `json_value`, im JSON aber `json` (Alias) |
| `CalcParamsDto` | [CalcParamsDto](../../referenz-plugin-java/dtos/CalcParamsDto/index.md) | Standardwerte, siehe unten |
| `ImageBase64Dto` | [ImageBase64Dto](../../referenz-plugin-java/dtos/ImageBase64Dto/index.md) | – |
| `ImageInfoDto` | [ImageInfoDto](../../referenz-plugin-java/dtos/ImageInfoDto/index.md) | **`pluginType` statt `pluginTyp`**; `lifetime` Standard 0 |
| `ImageUrlDto` | [ImageUrlDto](../../referenz-plugin-java/dtos/ImageUrlDto/index.md) | **`imageInfo` statt `imageInfoDto`**; wird von keinem Endpunkt verwendet |
| `JavascriptLibrary` | [JavascriptLibrary](../../referenz-plugin-java/dtos/JavascriptLibrary/index.md) | – |
| `LoadPluginRequestDto` | [LoadPluginRequestDto](../../referenz-plugin-java/dtos/LoadPluginRequestDto/index.md) | – |
| `PluginAngabeRequestDto` | [PluginAngabeRequestDto](../../referenz-plugin-java/dtos/PluginAngabeRequestDto/index.md) | – |
| `PluginAnswerDto` | [PluginAnswerDto](../../referenz-plugin-java/dtos/PluginAnswerDto/index.md) | – |
| `PluginConfigDto` | [PluginConfigDto](../../referenz-plugin-java/dtos/PluginConfigDto/index.md) | `params` mit beliebigen Werten (`Dict[str, Any]`) |
| `PluginConfigurationInfoDto` | [PluginConfigurationInfoDto](../../referenz-plugin-java/dtos/PluginConfigurationInfoDto/index.md) | Standardwerte, siehe unten; die Konstanten `CONFIGMODE_*` stehen in `PluginDemo` |
| `PluginConfigurationInfoRequestDto` | [PluginConfigurationInfoRequestDto](../../referenz-plugin-java/dtos/PluginConfigurationInfoRequestDto/index.md) | `timeout` Standard 300 |
| `PluginConfigurationRequestDto` | [PluginConfigurationRequestDto](../../referenz-plugin-java/dtos/PluginConfigurationRequestDto/index.md) | – |
| `PluginDatasetDto` | [PluginDatasetDto](../../referenz-plugin-java/dtos/PluginDatasetDto/index.md) | – |
| `PluginDatasetListDto` | [PluginDatasetListDto](../../referenz-plugin-java/dtos/PluginDatasetListDto/index.md) | – |
| `PluginDto` | [PluginDto](../../referenz-plugin-java/dtos/PluginDto/index.md) | – |
| `PluginEinheitRequestDto` | [PluginEinheitRequestDto](../../referenz-plugin-java/dtos/PluginEinheitRequestDto/index.md) | – |
| `PluginGeneralInfo` | [PluginGeneralInfo](../../referenz-plugin-java/dtos/PluginGeneralInfo/index.md) | Standardwerte, siehe unten |
| `PluginGeneralInfoList` | [PluginGeneralInfoList](../../referenz-plugin-java/dtos/PluginGeneralInfoList/index.md) | – |
| `PluginMaximaCalcModeDto` | [PluginMaximaCalcModeDto](../../referenz-plugin-java/dtos/PluginMaximaCalcModeDto/index.md) | `preCalc` Standard `false` (Java `true`) |
| `PluginParserRequestDto` | [PluginParserRequestDto](../../referenz-plugin-java/dtos/PluginParserRequestDto/index.md) | – |
| `PluginQuestionDto` | [PluginQuestionDto](../../referenz-plugin-java/dtos/PluginQuestionDto/index.md) | – |
| `PluginRenderDto` | [PluginRenderDto](../../referenz-plugin-java/dtos/PluginRenderDto/index.md) | – |
| `PluginRenderLatexRequestDto` | [PluginRenderLatexRequestDto](../../referenz-plugin-java/dtos/PluginRenderLatexRequestDto/index.md) | `mode` Standard `"default"` |
| `PluginRenderResultRequestDto` | [PluginRenderResultRequestDto](../../referenz-plugin-java/dtos/PluginRenderResultRequestDto/index.md) | `grade` Standard 1.0 |
| `PluginRequestDto` | [PluginRequestDto](../../referenz-plugin-java/dtos/PluginRequestDto/index.md) | – |
| `PluginScoreInfoDto` | [PluginScoreInfoDto](../../referenz-plugin-java/dtos/PluginScoreInfoDto/index.md) | `status` als String, Standard `"FALSCH"` |
| `PluginScoreRequestDto` | [PluginScoreRequestDto](../../referenz-plugin-java/dtos/PluginScoreRequestDto/index.md) | `grade` Standard 1.0 |
| `PluginSetConfigurationDataRequestDto` | [PluginSetConfigurationDataRequestDto](../../referenz-plugin-java/dtos/PluginSetConfigurationDataRequestDto/index.md) | – |
| `PluginSubQuestionDto` | [PluginSubQuestionDto](../../referenz-plugin-java/dtos/PluginSubQuestionDto/index.md) | – |
| `PluginUpdateJavascriptRequestDto` | [PluginUpdateJavascriptRequestDto](../../referenz-plugin-java/dtos/PluginUpdateJavascriptRequestDto/index.md) | – |
| `ServiceInfoDTO` | [ServiceInfoDTO](../../referenz-plugin-java/dtos/ServiceInfoDTO/index.md) | Felder gleich, Inhalt reduziert (siehe [REST-Schnittstelle](../rest-schnittstelle/index.md)) |
| `ToleranzDto` | [ToleranzDto](../../referenz-plugin-java/dtos/ToleranzDto/index.md) | – |
| `VarDto` | [VarDto](../../referenz-plugin-java/dtos/VarDto/index.md) | – |
| `VarHashDto` | [VarHashDto](../../referenz-plugin-java/dtos/VarHashDto/index.md) | – |

## Ohne eigenes Pydantic-Modell

| Java-Klasse | in Python |
|---|---|
| [ConfigServiceDto](../../referenz-plugin-java/dtos/ConfigServiceDto/index.md) | Dictionary in `_build_registration_payload`, zusätzlich mit `htmlServiceStartTime` und `htmlLastRegistrationTime` – siehe [Build und Deployment](../build-deployment/index.md#registrierung-am-letto-server) |
| [RegisterServiceResultDto](../../referenz-plugin-java/dtos/RegisterServiceResultDto/index.md) | Antwort des Setups wird nicht ausgewertet |
| [PluginConfigurationConnection](../../referenz-plugin-java/dtos/PluginConfigurationConnection/index.md) | Dataclass `PluginConfigurationState` (zusätzlich `touch()` und `is_expired()`) |
| [PluginImageResultDto](../../referenz-plugin-java/dtos/PluginImageResultDto/index.md) | nicht vorhanden; Fehler beim Bild stehen direkt in `ImageBase64Dto.error` |

## AdminInfoDto

Die Python-Version hat ein eigenes, kleineres `AdminInfoDto`. Gemeinsam sind nur `pid`, `version`, `encoding`, `javaVersion` und `ip`.

| Feld | Typ | Standard |
|---|---|---|
| `applicationname` | str | `plugindemopython` |
| `pid` | int | 0 |
| `applicationhome` | str | `""` |
| `startupDate` | int | 0 |
| `uptime` | int | 0 |
| `version` | str | `python` |
| `servername` | str | `""` |
| `system` | str | `""` |
| `encoding` | str | `""` |
| `javaVersion` | str | `""` |
| `ip` | str | `""` |
| `dockerName` | str | `""` |
| `uriIntern` | str | `""` |
| `uriInternEnabled` | bool | `true` |
| `uriExtern` | str | `""` |
| `uriExternEnabled` | bool | `true` |

Der `/info`-Endpunkt setzt davon nur `applicationname`.

## Abweichende Standardwerte

Standardwerte wirken nur, wenn ein Feld im Request fehlt bzw. das Plugin es nicht setzt.

| DTO | Feld | Python | Java |
|---|---|---|---|
| `CalcParamsDto` | `rekursiv`, `ausmultiplizieren`, `herausheben`, `forceOpt` | `true` | `false` |
| `CalcParamsDto` | `showpotenz`, `calcmode` | `"AUTO"`, `"MAXIMA"` | `null` |
| `PluginGeneralInfo` | `defaultPluginConfig` | `false` | `true` |
| `PluginGeneralInfo` | `javaScript`, `inputElement` | `true`, `"JAVASCRIPT"` | `false`, `"TextField"` |
| `PluginGeneralInfo` | `pluginType` | `"python.PluginDemo"` | `""` |
| `PluginConfigurationInfoDto` | `useVars`, `useCVars`, `useMaximaVars`, `useMVars` | `true` | `false` |
| `PluginConfigDto` | `tagName` | `"plugintag"` | `""` |
| `PluginMaximaCalcModeDto` | `preCalc` | `false` | `true` |
| `ImageInfoDto` | `lifetime` | 0 (kein Ablauf) | ein Jahr ab Erzeugung |

[Referenz-Plugin (Python)](../index.md)
