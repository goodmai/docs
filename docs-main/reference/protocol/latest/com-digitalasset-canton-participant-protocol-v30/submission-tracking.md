---
title: "submission_tracking.proto"
description: "Markdown extract for com.digitalasset.canton.participant.protocol.v30 / community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto."
---

# `community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30)
- Package set: [com.digitalasset.canton.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30) | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | `com.digitalasset.canton.participant.protocol.v30` | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto)

## Related sections in this package

- [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/party_replication.proto](/reference/protocol/latest/com-digitalasset-canton-participant-protocol-v30/party-replication)

## Types in this section

- [com.digitalasset.canton.participant.protocol.v30.CommandRejected](#type-com-digitalasset-canton-participant-protocol-v30-commandrejected)
- [com.digitalasset.canton.participant.protocol.v30.CommandRejected.GrpcRejectionReasonTemplate](#type-com-digitalasset-canton-participant-protocol-v30-commandrejected-grpcrejectionreasontemplate)
- [com.digitalasset.canton.participant.protocol.v30.CompletionInfo](#type-com-digitalasset-canton-participant-protocol-v30-completioninfo)
- [com.digitalasset.canton.participant.protocol.v30.SubmissionTrackingData](#type-com-digitalasset-canton-participant-protocol-v30-submissiontrackingdata)
- [com.digitalasset.canton.participant.protocol.v30.TransactionSubmissionTrackingData](#type-com-digitalasset-canton-participant-protocol-v30-transactionsubmissiontrackingdata)
- [com.digitalasset.canton.participant.protocol.v30.TransactionSubmissionTrackingData.RejectionCause](#type-com-digitalasset-canton-participant-protocol-v30-transactionsubmissiontrackingdata-rejectioncause)

## Extracted reference

<a id="type-com-digitalasset-canton-participant-protocol-v30-commandrejected"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.CommandRejected`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto)
- Fields: 0

_No description._

<a id="type-com-digitalasset-canton-participant-protocol-v30-commandrejected-grpcrejectionreasontemplate"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.CommandRejected.GrpcRejectionReasonTemplate`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| status | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-participant-protocol-v30-completioninfo"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.CompletionInfo`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| act_as | `string` | repeated |  |
| user_id | `string` | optional |  |
| command_id | `string` | optional |  |
| opt_deduplication_period | [`com.digitalasset.canton.protocol.v30.DeduplicationPeriod`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction#type-com-digitalasset-canton-protocol-v30-deduplicationperiod) | optional |  |
| submission_id | `string` | optional |  |

<a id="type-com-digitalasset-canton-participant-protocol-v30-submissiontrackingdata"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.SubmissionTrackingData`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| transaction | [`com.digitalasset.canton.participant.protocol.v30.TransactionSubmissionTrackingData`](#type-com-digitalasset-canton-participant-protocol-v30-transactionsubmissiontrackingdata) | optional |  |

<a id="type-com-digitalasset-canton-participant-protocol-v30-transactionsubmissiontrackingdata"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.TransactionSubmissionTrackingData`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| completion_info | [`com.digitalasset.canton.participant.protocol.v30.CompletionInfo`](#type-com-digitalasset-canton-participant-protocol-v30-completioninfo) | optional |  |
| rejection_cause | [`com.digitalasset.canton.participant.protocol.v30.TransactionSubmissionTrackingData.RejectionCause`](#type-com-digitalasset-canton-participant-protocol-v30-transactionsubmissiontrackingdata-rejectioncause) | optional |  |
| physical_synchronizer_id | `string` | optional |  |

<a id="type-com-digitalasset-canton-participant-protocol-v30-transactionsubmissiontrackingdata-rejectioncause"></a>
**Message `com.digitalasset.canton.participant.protocol.v30.TransactionSubmissionTrackingData.RejectionCause`**

- Source: [community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/participant/src/main/protobuf/com/digitalasset/canton/participant/protocol/v30/submission_tracking.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| timeout | `google.protobuf.Empty` | optional |  |
| rejection_reason_template | [`com.digitalasset.canton.participant.protocol.v30.CommandRejected.GrpcRejectionReasonTemplate`](#type-com-digitalasset-canton-participant-protocol-v30-commandrejected-grpcrejectionreasontemplate) | optional |  |
