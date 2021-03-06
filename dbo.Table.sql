CREATE TABLE [dbo].[Table]
(
	[Id] INT NOT NULL PRIMARY KEY, 
    [regId]    INTEGER NOT NULL,
    [name]    TEXT NOT NULL,
    [dateBirthDay]    TEXT NOT NULL,
    [passportSeries]    INTEGER NOT NULL,
    [passportNumbe]    INTEGER NOT NULL,
    [passportIssuedByWhom]    TEXT NOT NULL,
    [residenceAddress]    TEXT NOT NULL,
    [residentialAddress]    TEXT NOT NULL,
    [theRightToPriorityParticipation]    TEXT NOT NULL,
    [telephone]    TEXT NOT NULL,
    [e-mail]    TEXT NOT NULL,
    [institute]    TEXT NOT NULL,
    [specialtyCode]    TEXT NOT NULL,
    [course]    INTEGER NOT NULL,
    [endDateYear]    INTEGER,
    [endDateMonth]    TEXT,
    [militarySpecialtyCode]    INTEGER NOT NULL,
)
