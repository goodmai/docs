---
title: "sequencing.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/mediator)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/ordering_request.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/ordering-request)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-reassignment)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/quorum.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/quorum)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/signed_content.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/signed-content)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/storage.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/storage)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronization)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronizer-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.Batch](#type-com-digitalasset-canton-protocol-v30-batch)
- [com.digitalasset.canton.protocol.v30.CompressedBatch](#type-com-digitalasset-canton-protocol-v30-compressedbatch)
- [com.digitalasset.canton.protocol.v30.CompressedBatch.CompressionAlgorithm](#type-com-digitalasset-canton-protocol-v30-compressedbatch-compressionalgorithm)
- [com.digitalasset.canton.protocol.v30.Envelope](#type-com-digitalasset-canton-protocol-v30-envelope)
- [com.digitalasset.canton.protocol.v30.PossiblyIgnoredSequencedEvent](#type-com-digitalasset-canton-protocol-v30-possiblyignoredsequencedevent)
- [com.digitalasset.canton.protocol.v30.Recipients](#type-com-digitalasset-canton-protocol-v30-recipients)
- [com.digitalasset.canton.protocol.v30.RecipientsTree](#type-com-digitalasset-canton-protocol-v30-recipientstree)
- [com.digitalasset.canton.protocol.v30.SequencedEvent](#type-com-digitalasset-canton-protocol-v30-sequencedevent)
- [com.digitalasset.canton.protocol.v30.SequencingSubmissionCost](#type-com-digitalasset-canton-protocol-v30-sequencingsubmissioncost)
- [com.digitalasset.canton.protocol.v30.ServiceAgreement](#type-com-digitalasset-canton-protocol-v30-serviceagreement)
- [com.digitalasset.canton.protocol.v30.StaticSynchronizerParameters](#type-com-digitalasset-canton-protocol-v30-staticsynchronizerparameters)
- [com.digitalasset.canton.protocol.v30.SubmissionRequest](#type-com-digitalasset-canton-protocol-v30-submissionrequest)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-batch"></a>
**Message `com.digitalasset.canton.protocol.v30.Batch`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| envelopes | [`com.digitalasset.canton.protocol.v30.Envelope`](#type-com-digitalasset-canton-protocol-v30-envelope) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-compressedbatch"></a>
**Message `com.digitalasset.canton.protocol.v30.CompressedBatch`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| algorithm | [`com.digitalasset.canton.protocol.v30.CompressedBatch.CompressionAlgorithm`](#type-com-digitalasset-canton-protocol-v30-compressedbatch-compressionalgorithm) | optional |  |
| compressed_batch | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-compressedbatch-compressionalgorithm"></a>
**Enum `com.digitalasset.canton.protocol.v30.CompressedBatch.CompressionAlgorithm`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)

_No description._

| Name | Number |
| --- | --- |
| COMPRESSION_ALGORITHM_UNSPECIFIED | `0` |
| COMPRESSION_ALGORITHM_GZIP | `1` |

<a id="type-com-digitalasset-canton-protocol-v30-envelope"></a>
**Message `com.digitalasset.canton.protocol.v30.Envelope`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 3

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| content | `bytes` | optional |  |
| recipients | [`com.digitalasset.canton.protocol.v30.Recipients`](#type-com-digitalasset-canton-protocol-v30-recipients) | optional |  |
| signatures | [`com.digitalasset.canton.crypto.v30.Signature`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signature) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-possiblyignoredsequencedevent"></a>
**Message `com.digitalasset.canton.protocol.v30.PossiblyIgnoredSequencedEvent`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 5

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| counter | `int64` | optional |  |
| timestamp | `int64` | optional |  |
| trace_context | [`com.digitalasset.canton.v30.TraceContext`](com-digitalasset-canton-v30#type-com-digitalasset-canton-v30-tracecontext) | optional |  |
| is_ignored | `bool` | optional |  |
| underlying | `bytes` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-recipients"></a>
**Message `com.digitalasset.canton.protocol.v30.Recipients`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| recipients_tree | [`com.digitalasset.canton.protocol.v30.RecipientsTree`](#type-com-digitalasset-canton-protocol-v30-recipientstree) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-recipientstree"></a>
**Message `com.digitalasset.canton.protocol.v30.RecipientsTree`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| recipients | `string` | repeated |  |
| children | [`com.digitalasset.canton.protocol.v30.RecipientsTree`](#type-com-digitalasset-canton-protocol-v30-recipientstree) | repeated |  |

<a id="type-com-digitalasset-canton-protocol-v30-sequencedevent"></a>
**Message `com.digitalasset.canton.protocol.v30.SequencedEvent`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 8

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| previous_timestamp | `int64` | optional |  |
| timestamp | `int64` | optional |  |
| physical_synchronizer_id | `string` | optional |  |
| message_id | `string` | optional |  |
| batch | [`com.digitalasset.canton.protocol.v30.CompressedBatch`](#type-com-digitalasset-canton-protocol-v30-compressedbatch) | optional |  |
| deliver_error_reason | `google.rpc.Status` | optional |  |
| topology_timestamp | `int64` | optional |  |
| traffic_receipt | [`com.digitalasset.canton.protocol.v30.TrafficReceipt`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters#type-com-digitalasset-canton-protocol-v30-trafficreceipt) | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-sequencingsubmissioncost"></a>
**Message `com.digitalasset.canton.protocol.v30.SequencingSubmissionCost`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| cost | `int64` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-serviceagreement"></a>
**Message `com.digitalasset.canton.protocol.v30.ServiceAgreement`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| id | `string` | optional |  |
| legal_text | `string` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-staticsynchronizerparameters"></a>
**Message `com.digitalasset.canton.protocol.v30.StaticSynchronizerParameters`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 10

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| required_signing_specs | [`com.digitalasset.canton.crypto.v30.RequiredSigningSpecs`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-requiredsigningspecs) | optional |  |
| required_encryption_specs | [`com.digitalasset.canton.crypto.v30.RequiredEncryptionSpecs`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-requiredencryptionspecs) | optional |  |
| required_symmetric_key_schemes | [`com.digitalasset.canton.crypto.v30.SymmetricKeyScheme`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-symmetrickeyscheme) | repeated |  |
| required_hash_algorithms | [`com.digitalasset.canton.crypto.v30.HashAlgorithm`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-hashalgorithm) | repeated |  |
| required_crypto_key_formats | [`com.digitalasset.canton.crypto.v30.CryptoKeyFormat`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-cryptokeyformat) | repeated |  |
| required_signature_formats | [`com.digitalasset.canton.crypto.v30.SignatureFormat`](com-digitalasset-canton-crypto-v30#type-com-digitalasset-canton-crypto-v30-signatureformat) | repeated |  |
| protocol_version | `int32` | optional |  |
| serial | `int32` | optional |  |
| enable_transparency_checks | `bool` | optional |  |
| topology_change_delay | `google.protobuf.Duration` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-submissionrequest"></a>
**Message `com.digitalasset.canton.protocol.v30.SubmissionRequest`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto)
- Fields: 7

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| sender | `string` | optional |  |
| message_id | `string` | optional |  |
| batch | [`com.digitalasset.canton.protocol.v30.CompressedBatch`](#type-com-digitalasset-canton-protocol-v30-compressedbatch) | optional |  |
| max_sequencing_time | `int64` | optional |  |
| topology_timestamp | `int64` | optional |  |
| aggregation_rule | [`com.digitalasset.canton.protocol.v30.AggregationRule`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable#type-com-digitalasset-canton-protocol-v30-aggregationrule) | optional |  |
| submission_cost | [`com.digitalasset.canton.protocol.v30.SequencingSubmissionCost`](#type-com-digitalasset-canton-protocol-v30-sequencingsubmissioncost) | optional |  |
