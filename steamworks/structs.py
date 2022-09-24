from ctypes import *

import steamworks.constants as constants


class FindLeaderboardResult_t(Structure):
    """ Represents the STEAMWORKS LeaderboardFindResult_t call result type """
    _fields_ = [("leaderboardHandle", c_uint64), ("leaderboardFound", c_uint32)]


class CreateItemResult_t(Structure):
    _fields_ = [("result", c_int), ("publishedFileId", c_uint64),
                ("userNeedsToAcceptWorkshopLegalAgreement", c_bool)]


class SubmitItemUpdateResult_t(Structure):
    _fields_ = [("result", c_int), ("userNeedsToAcceptWorkshopLegalAgreement", c_bool),
                ("publishedFileId", c_uint64)]


class ItemInstalled_t(Structure):
    _fields_ = [("appId", c_uint32), ("publishedFileId", c_uint64)]


class SubscriptionResult(Structure):
    _fields_ = [("result", c_int32), ("publishedFileId", c_uint64)]


class SteamUGCQueryCompleted_t(Structure):
    _fields_ = [("handle", c_uint64), ("result", c_int), ("NumResultsReturned", c_uint32),
                ("TotalMatchingResults", c_uint32), ("CachedData", c_bool),
                ("NextCursor", c_char * constants.PublishedFileURLMax)]


class SteamUGCDetails_t(Structure):
    _fields_ = [
        ("PublishedFileId", c_uint64),
        ("result", c_int32),
        ("FileType", c_int32),
        ("CreatorAppID", c_uint32),
        ("ConsumerAppID", c_uint32),
        ("Title", c_char * constants.PublishedDocumentTitleMax),
        ("Description", c_char * constants.PublishedDocumentDescriptionMax),
        ("SteamIDOwner", c_uint64),
        ("timeCreated", c_uint32),
        ("timeUpdated", c_uint32),
        ("timeAddedToUserList", c_uint32),
        ("Visibility", c_int32),
        ("Banned", c_bool),
        ("AcceptedForUse", c_bool),
        ("TagsTruncated", c_bool),
        ("Tags", c_char * constants.TagListMax),
        ("File", c_uint64),
        ("PreviewFile", c_uint64),
        ("FileName", c_char * constants.FilenameMax),
        ("FileSize", c_int32),
        ("PreviewFileSize", c_int32),
        ("URL", c_char * constants.PublishedFileURLMax),
        ("VotesUp", c_uint32),
        ("VotesDown", c_uint32),
        ("Score", c_float),
        ("NumChildren", c_uint32),
    ]


class MicroTxnAuthorizationResponse_t(Structure):
    _fields_ = [("appId", c_uint32), ("orderId", c_uint64), ("authorized", c_bool)]
