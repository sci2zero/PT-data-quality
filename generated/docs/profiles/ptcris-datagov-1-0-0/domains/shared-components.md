# SHARED_COMPONENTS

## `Contact.contactEmail`

Validation Target: `VT.SHARED_COMPONENTS.Contact.ContactEmail`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Contact.ContactEmail.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Contact.contactEmail exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.ContactEmail.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Contact.contactEmail is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.ContactEmail.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Contact.contactEmail does not match the required format. | UNMAPPED |

## `Contact.faxNumber`

Validation Target: `VT.SHARED_COMPONENTS.Contact.FaxNumber`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Contact.FaxNumber.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Contact.faxNumber exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.FaxNumber.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Contact.faxNumber is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.FaxNumber.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Contact.faxNumber does not match the required format. | UNMAPPED |

## `Contact.mobilePhoneNumber`

Validation Target: `VT.SHARED_COMPONENTS.Contact.MobilePhoneNumber`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Contact.mobilePhoneNumber exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Contact.mobilePhoneNumber is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Contact.mobilePhoneNumber does not match the required format. | UNMAPPED |

## `Contact.phoneNumber`

Validation Target: `VT.SHARED_COMPONENTS.Contact.PhoneNumber`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Contact.PhoneNumber.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Contact.phoneNumber exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.PhoneNumber.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Contact.phoneNumber is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.PhoneNumber.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Contact.phoneNumber does not match the required format. | UNMAPPED |

## `Country.code`

Validation Target: `VT.SHARED_COMPONENTS.Country.Code`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Country.Code.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Country.code exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Country.code is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Country.code is required. | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Country.code must be unique within the repository. | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Country.code must belong to the configured controlled vocabulary. | GR.PTCRIS_F1_01DSEMANT.standardized_geopolitical_country_coding |

## `Currency.code`

Validation Target: `VT.SHARED_COMPONENTS.Currency.Code`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Currency.Code.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Currency.code exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Currency.code is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Currency.code is required. | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Currency.code does not match the required format. | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Currency.code must be unique within the repository. | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Currency.code must belong to the configured controlled vocabulary. | UNMAPPED |

## `Currency.symbol`

Validation Target: `VT.SHARED_COMPONENTS.Currency.Symbol`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Currency.Symbol.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Currency.symbol exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Symbol.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Currency.symbol is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Symbol.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Currency.symbol must belong to the configured controlled vocabulary. | UNMAPPED |

## `EntityIndicator.numericValue, booleanValue, textualValue`

Validation Target: `VT.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | An entity indicator must contain at least one value compatible with the linked indicator content type: numeric, boolean, or textual. | UNMAPPED |
| C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for EntityIndicator.numericValue, booleanValue, textualValue is required. | UNMAPPED |

## `EntityIndicator.subclass`

Validation Target: `VT.SHARED_COMPONENTS.EntityIndicator.Subclass`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.EntityIndicator.Subclass.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | The entity-indicator subclass must be compatible with the applicable types of the linked indicator. | UNMAPPED |

## `FlexibleDate.day`

Validation Target: `VT.SHARED_COMPONENTS.FlexibleDate.Day`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.FlexibleDate.Day.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | The day value must be valid for the selected month. | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Day.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of FlexibleDate.day exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Day.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of FlexibleDate.day is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Day.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for FlexibleDate.day is recommended. | UNMAPPED |

## `FlexibleDate.month`

Validation Target: `VT.SHARED_COMPONENTS.FlexibleDate.Month`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.FlexibleDate.Month.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of FlexibleDate.month exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Month.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of FlexibleDate.month is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Month.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for FlexibleDate.month is recommended. | UNMAPPED |

## `FlexibleDate.text, year`

Validation Target: `VT.SHARED_COMPONENTS.FlexibleDate.TextYear`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.FlexibleDate.TextYear.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | A flexible date must contain at least a year or a textual date representation. | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.TextYear.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for FlexibleDate.text, year is required. | UNMAPPED |

## `FlexibleDate.year`

Validation Target: `VT.SHARED_COMPONENTS.FlexibleDate.Year`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.FlexibleDate.Year.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of FlexibleDate.year exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Year.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of FlexibleDate.year is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Year.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for FlexibleDate.year is recommended. | UNMAPPED |

## `GeoLocation.address`

Validation Target: `VT.SHARED_COMPONENTS.GeoLocation.Address`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.GeoLocation.Address.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for GeoLocation.address is recommended. | UNMAPPED |

## `GeoLocation.latitude`

Validation Target: `VT.SHARED_COMPONENTS.GeoLocation.Latitude`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.GeoLocation.Latitude.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of GeoLocation.latitude exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Latitude.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of GeoLocation.latitude is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Latitude.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for GeoLocation.latitude is required. | UNMAPPED |

## `GeoLocation.longitude`

Validation Target: `VT.SHARED_COMPONENTS.GeoLocation.Longitude`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.GeoLocation.Longitude.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of GeoLocation.longitude exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Longitude.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of GeoLocation.longitude is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Longitude.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for GeoLocation.longitude is required. | UNMAPPED |

## `Identifier.regularExpression`

Validation Target: `VT.SHARED_COMPONENTS.Identifier.RegularExpression`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Identifier.RegularExpression.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | The configured regular expression must be syntactically valid. | UNMAPPED |
| C.SHARED_COMPONENTS.Identifier.RegularExpression.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Identifier.regularExpression exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Identifier.RegularExpression.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Identifier.regularExpression is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Identifier.RegularExpression.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Identifier.regularExpression is recommended. | UNMAPPED |

## `Language.languageCode`

Validation Target: `VT.SHARED_COMPONENTS.Language.LanguageCode`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.Language.LanguageCode.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Language.languageCode exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Language.languageCode is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Language.languageCode is required. | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Language.languageCode does not match the required format. | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Language.languageCode must be unique within the repository. | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Language.languageCode must belong to the configured controlled vocabulary. | UNMAPPED |

## `LanguageTag.languageTag`

Validation Target: `VT.SHARED_COMPONENTS.LanguageTag.LanguageTag`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of LanguageTag.languageTag exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of LanguageTag.languageTag is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for LanguageTag.languageTag is required. | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of LanguageTag.languageTag does not match the required format. | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of LanguageTag.languageTag must be unique within the repository. | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of LanguageTag.languageTag must belong to the configured controlled vocabulary. | UNMAPPED |

## `MonetaryAmount.amount`

Validation Target: `VT.SHARED_COMPONENTS.MonetaryAmount.Amount`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.MonetaryAmount.Amount.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of MonetaryAmount.amount exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.MonetaryAmount.Amount.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of MonetaryAmount.amount is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.MonetaryAmount.Amount.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for MonetaryAmount.amount is required. | UNMAPPED |

## `ProfilePhotoOrLogo.height`

Validation Target: `VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ProfilePhotoOrLogo.height exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ProfilePhotoOrLogo.height is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for ProfilePhotoOrLogo.height is required. | UNMAPPED |

## `ProfilePhotoOrLogo.leftOffset`

Validation Target: `VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ProfilePhotoOrLogo.leftOffset exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ProfilePhotoOrLogo.leftOffset is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for ProfilePhotoOrLogo.leftOffset is required. | UNMAPPED |

## `ProfilePhotoOrLogo.topOffset`

Validation Target: `VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ProfilePhotoOrLogo.topOffset exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ProfilePhotoOrLogo.topOffset is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for ProfilePhotoOrLogo.topOffset is required. | UNMAPPED |

## `ProfilePhotoOrLogo.width`

Validation Target: `VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ProfilePhotoOrLogo.width exceeds the maximum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ProfilePhotoOrLogo.width is below the minimum allowed value. | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for ProfilePhotoOrLogo.width is required. | UNMAPPED |

## `ResearchArea.name`

Validation Target: `VT.SHARED_COMPONENTS.ResearchArea.Name`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.SHARED_COMPONENTS.ResearchArea.Name.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of ResearchArea.name exceeds the maximum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.ResearchArea.Name.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of ResearchArea.name is shorter than the minimum allowed length. | UNMAPPED |
| C.SHARED_COMPONENTS.ResearchArea.Name.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for ResearchArea.name is required. | UNMAPPED |
| C.SHARED_COMPONENTS.ResearchArea.Name.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of ResearchArea.name must belong to the configured controlled vocabulary. | UNMAPPED |
